# Issue Documentation Table

| Issue | Type | Line(s) (Original) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| **SQL Injection Vulnerability** | Security / Bug (Bandit) | 10 | String interpolation (`%s`) used in SQL queries allows for SQL injection attacks. | Replaced string formatting with parameterized queries (`?`) using SQLite's built-in tuple substitution. |
| **Mutable Default Argument** | Bug / Quality (Pylint) | 9 | `tags=[]` is evaluated once at function definition, meaning the same list is shared across all calls. | Changed the default argument to `tags=None` and initialized `tags = []` inside the function block. |
| **Weak Cryptographic PRNG** | Security (Bandit) | 21 | `random.randint` is a weak pseudo-random number generator, making it unsuitable for secure tokens. | Imported the `secrets` module and replaced `random.randint` with `secrets.choice()` for cryptographically secure generation. |
| **Bare and Broad Exceptions** | Logic / Style (Flake8 / Pylint) | 27, 33 | `except:` and `except Exception:` catch everything, including system exits and keyboard interrupts, hiding critical errors. | Changed to specifically catch `sqlite3.Error` and added proper `None` checks for the database `.fetchone()` return value. |
| **PEP 8 Naming & Formatting** | Style (Flake8 / Pylint) | 9, 13, 20, 39 | camelCase function names and multiple statements on a single line violate PEP 8 standards. | Converted names to `snake_case` (e.g., `registerPet` to `register_pet`), added docstrings, and separated inline `if` statements onto multiple lines. |
