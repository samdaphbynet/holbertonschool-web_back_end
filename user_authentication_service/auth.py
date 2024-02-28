#!/usr/bin/env python3
"""
Hash password
"""
import uuid
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

    def valid_login(self, email: str, password: str) -> bool:
        """
        function to validate a user's login credentials
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode("utf-8"),
                                  user.hashed_password)
        except NoResultFound:
            return False


def _generate_uuid() -> str:
    """
    function to generate a uuid for the user
    """
    return str(uuid.uuid4())


def _hash_password(password: str) -> str:
    """
    function to hash password using sha256 algorithm
    """

    hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    return hash
