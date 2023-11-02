import bcrypt
"""
encrypt_password.py - Encrypting passwords
"""


def hash_password(password: str) -> bytes:
    """
    Hashes a password with bcrypt.

    Arguments:
    password -- The password to hash.

    Returns:
    A byte string representing the hashed password.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password
