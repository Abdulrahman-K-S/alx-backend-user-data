#!/usr/bin/env python3
"""
Task 5. Encrypting passwords

Encrypt the passwords
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """has_password

    This method hashes a password as to be more encrypted.

    Arguments:
        password (str): The password to encrypt.

    Return:
        (bytes): The hashed password in bytes.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
