import bcrypt
"""
encrypt_password.py - Encrypting passwords
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password with bcrypt.

    Arguments:
    password -- The password to hash.

    Returns:
    A byte string representing the hashed password.
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed
