#!/usr/bin/env python3
"""
Module for handling Personal Data
"""
import re
from typing import List
import logging


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


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class that obfuscates specified fields in log records.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        """
        Initializes the formatter with the fields to obfuscate.

        Arguments:
        fields -- List of field names that should be obfuscated.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record by obfuscating specified fields.

        Arguments:
        record -- The log record to format.

        Returns:
        The formatted log record with specified fields obfuscated.
        """
        original_message = logging.Formatter.format(self, record)
        return filter_datum(
            self.fields, self.REDACTION, original_message, self.SEPARATOR
        )
