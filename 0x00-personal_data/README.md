# 0x00. Personal Data (Back-end | Authentication)

This is a project based on the 0x00 module of the Holberton School's Back-end curriculum, focusing on personal data protection and authentication. The project consists of several tasks, and we'll guide you through each one.

## Requirements

- All code should be written and tested on Ubuntu 18.04 LTS using Python 3.7.
- Ensure all your code files end with a newline.
- The first line of every code file should be `#!/usr/bin/env python3`.
- Include a `README.md` file at the root of your project folder.
- Use `pycodestyle` style (version 2.5) for your code.
- All your code files must be executable.
- File lengths will be checked using `wc`.
- All modules, classes, and functions should have documentation.
- Use type annotations for all functions.
- Documentation should provide a clear explanation of the purpose of the module, class, or method.
- Functions should be implemented following the provided requirements.

## Tasks

### 0. Regex-ing

- Write a function `filter_datum` that obfuscates personal data in log messages.
- Arguments:
  - `fields`: a list of strings representing fields to obfuscate.
  - `redaction`: a string representing how the field will be obfuscated.
  - `message`: a string representing the log line.
  - `separator`: a string representing the character separating fields in the log line.
- Use a regex to replace occurrences of certain field values.
- `filter_datum` should be less than 5 lines long and use `re.sub` to perform the substitution with a single regex.

### 1. Log formatter

- Modify a class `RedactingFormatter` that subclasses `logging.Formatter`.
- The class should accept a list of strings `fields` as a constructor argument.
- Implement the `format` method to filter values in incoming log records using `filter_datum`.
- The `format` method should be less than 5 lines long.

### 2. Create logger

- Implement a `get_logger` function that returns a `logging.Logger` object.
- The logger should be named "user_data" and only log up to `logging.INFO` level.
- The logger should not propagate messages to other loggers.
- It should have a `StreamHandler` with `RedactingFormatter` as the formatter.
- Create a constant `PII_FIELDS` containing the fields from `user_data.csv` that are considered PII.

### 3. Connect to secure database

- Create a function `get_db` that returns a connection to a secure database.
- Use the `os` module to obtain credentials from environment variables.
- Use the `mysql-connector-python` module to connect to the MySQL database.

### 4. Read and filter data

- Implement a `main` function that retrieves data from a database and logs it.
- The function should obtain a database connection using `get_db`.
- Retrieve all rows from the `users` table and log each row with PII fields filtered.
- Run only your `main` function when the module is executed.

### 5. Encrypting passwords

- Implement a `hash_password` function that takes a password as input and returns a salted, hashed password.
- Use the `bcrypt` package to perform the hashing.

### 6. Check valid password

- Implement an `is_valid` function that checks if a password matches a hashed password.
- Use `bcrypt` to validate the provided password against the hashed password.

## Usage

You can use the provided example code to test your implementations for each task. Remember to use environment variables for sensitive information and protect personal data in your logs.

## Author

This project is part of the Holberton School curriculum and was created by the Holberton School team.
