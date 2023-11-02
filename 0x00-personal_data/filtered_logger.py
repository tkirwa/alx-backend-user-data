#!/usr/bin/env python3
"""
Module for handling Personal Data
"""
import re
from typing import List


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
