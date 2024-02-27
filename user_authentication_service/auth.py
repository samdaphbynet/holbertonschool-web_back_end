#!/usr/bin/env python3
"""
Hash password
"""
import bcrypt


def _hash_password(password) -> bytes:
    """
    function to hash password using sha256 algorithm
    """

    hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    return hash
