#!/usr/bin/env python3
"""
Module for handling Personal Data
"""
import re
from typing import List
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Obfuscates specified fields in a message.

    Arguments:
    fields -- List of field names that should be obfuscated.
    redaction -- The value that should replace the obfuscated fields.
    message -- The message that contains the fields.
    separator -- The character that separates fields in the message.

    Returns:
    The message with the specified fields obfuscated.
    """
    for f in fields:
        message = re.sub(f"{f}=.*?{separator}",
                         f"{f}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:
    """
    Creates and returns a logger object with specific settings.

    The logger object is named "user_data" and its level is set to INFO.
    Propagation is turned off to prevent the log messages from being passed
    to the root logger. A stream handler with a specific formatter is added
    to the logger. This formatter obfuscates fields defined in PII_FIELDS.

    Returns:
        logging.Logger: The configured logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Establishes a connection to a MySQL database.

    Uses the following environment variables for the database credentials:
    - PERSONAL_DATA_DB_USERNAME: The username for the database
      (default is "root").
    - PERSONAL_DATA_DB_PASSWORD: The password for the database
      (default is an empty string).
    - PERSONAL_DATA_DB_HOST: The host of the database
      (default is "localhost").
    - PERSONAL_DATA_DB_NAME: The name of the database.

    Returns:
        A MySQLConnection object representing the established
          database connection.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    db = mysql.connector.connect(
        user=username, password=password, host=host, database=db_name
    )

    return db


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters values in incoming log records using filter_datum"""
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR
        )
        return super(RedactingFormatter, self).format(record)


if __name__ == "__main__":
    main()
