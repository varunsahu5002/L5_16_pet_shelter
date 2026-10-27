Reflect on the contribution of static analysis to overall code quality and maintainability.
Static code analysis acts as an automated first line of defense before the software ever runs. Pylint enforces logical consistency by catching structural errors like mutable default arguments that often lead to difficult-to-trace state bugs. Bandit provides an essential security audit by automatically flagging vulnerabilities like SQL injection patterns and weak random number generation, which manual reviewers might overlook. Finally, Flake8 guarantees standard PEP 8 formatting. This standardizes the codebase layout, ensuring that developers reading the code in the future can focus on the logic rather than untangling inconsistent styling, thereby heavily reducing long-term maintainability costs. 


How do Pylint, Flake8, and Bandit differ in their specific roles during static code analysis?
While all three are static analysis tools, they serve different primary purposes. Pylint acts as a strict code reviewer focused on logical errors, code quality, and poor design practices. Flake8 functions as a grammar checker that strictly enforces PEP 8 style guidelines, checking for formatting, whitespace, and line length issues. Bandit acts as a security guard, specifically scanning the code for known vulnerabilities and insecure coding patterns rather than style or logic. 


What specific security vulnerabilities were identified in the original script, and why were they dangerous?
Bandit identified two primary security risks. First, the use of string interpolation (%s) in the database INSERT statement created an SQL injection vulnerability, which could allow a malicious user to execute arbitrary database commands. Second, it flagged the use of random.randint for generating adoption codes, which is a weak pseudo-random number generator unsuitable for secure or unpredictable token generation. 


Why is a mutable default argument (like tags=[]) considered a bad practice in Python, as flagged by Pylint?
In Python, default arguments are evaluated only once when the function is initially defined, not each time the function is called. By using a mutable object like a list for the tags parameter, every call to the registerPet function that omits this argument ends up sharing and modifying the exact same list in memory, leading to unpredictable state bugs and data leakage between function calls. 

