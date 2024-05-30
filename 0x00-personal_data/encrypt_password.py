#!/usr/bin/env python3
"""
Task 5. Encrypting passwords & 6. Check valid password

Encrypt the passwords & check if it's the hashed password or not.
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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """is_valid

    Checks whether the hashed password is the same as the
    passed password and returns a bool accordingly.

    Arguments:
        hashed_password (bytes):
        password (str):

    Return:
        (bool): [True: if the hashed password is equal to password/
                 False: if the hashed password isn't equal to password]
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
