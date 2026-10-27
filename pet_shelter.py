"""
Pet Shelter Management Module.
Handles pet registration, adoption, and shelter status tracking.
"""

import secrets
import sqlite3

# Initialize in-memory SQLite database
conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE pets "
    "(id INTEGER PRIMARY KEY, name TEXT, species TEXT, age INTEGER, adopted INTEGER)"
)
adoption_count = 0


def register_pet(name, species, age, tags=None):
    """Registers a new pet into the shelter database."""
    if tags is None:
        tags = []

    conn.execute(
        "INSERT INTO pets (name, species, age, adopted) VALUES (?, ?, ?, 0)",
        (name, species, age)
    )
    tags.append(species)
    return tags


def adopt(pet_id):
    """Marks a pet as adopted and increments the adoption count."""
    global adoption_count  # pylint: disable=global-statement
    conn.execute("UPDATE pets SET adopted = 1 WHERE id = ?", (pet_id,))
    adoption_count += 1


def adoption_code():
    """Generates a secure random adoption code."""
    code_number = secrets.choice(range(1000, 10000))
    return f"PET-{code_number}"


def oldest_available():
    """Returns the name of the oldest available pet."""
    try:
        row = conn.execute(
            "SELECT name, age FROM pets WHERE adopted = 0 ORDER BY age DESC"
        ).fetchone()
        if row:
            return row[0]
        return None
    except sqlite3.Error:
        return None


def clear_unadopted():
    """Removes all unadopted pets from the database."""
    try:
        conn.execute("DELETE FROM pets WHERE adopted = 0")
    except sqlite3.Error:
        pass


def shelter_status():
    """Returns the status of the shelter based on adoptions."""
    if adoption_count > 0:
        return "active"
    return "quiet"


def main():
    """Main execution function for the shelter script."""
    register_pet("Bruno", "dog", 7)
    register_pet("Mitzi", "cat", 3)
    register_pet("Kiwi", "parrot", 12)
    
    adopt(1)
    
    print(oldest_available(), adoption_code(), shelter_status())
    
    clear_unadopted()


if __name__ == "__main__":
    main()