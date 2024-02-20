#!/usr/bin/env python3
"""
User passwords should NEVER be stored in plain text in a database.
"""
import bcrypt


def hash_password(password):
    """
    hash_password function that expects one string argument name password and
    returns a salted, hashed password, which is a byte string.
    """
    hach = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hach
