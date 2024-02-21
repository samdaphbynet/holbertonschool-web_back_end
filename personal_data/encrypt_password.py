#!/usr/bin/env python3
"""
User passwords should NEVER be stored in plain text in a database.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    hash_password function that expects one string argument name password and
    returns a salted, hashed password, which is a byte string.
    """
    hach = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hach


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    is_valid function that expects 2 arguments and returns a boolean.

        Arguments:
        hashed_password: bytes type
        password: string type
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
