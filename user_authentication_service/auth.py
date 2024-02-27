#!/usr/bin/env python3
"""
Hash password
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        function to register a new user in the database
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hash = _hash_password(password)
            user = self._db.add_user(email, hash)

            return user

        else:
            raise ValueError(f"User {email} already exists")


def _hash_password(password: str) -> str:
    """
    function to hash password using sha256 algorithm
    """

    hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    return hash
