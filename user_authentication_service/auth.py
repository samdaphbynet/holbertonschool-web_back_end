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

    def create_session(self, email: str) -> str:
        """
        function to generate a session id for a user
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id) -> str:
        """ function to get a user from a session id """
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        else:
            return user

    def destroy_session(self, user_id: int) -> None:
        """
        function to destroy the session
        """
        if user_id is None:
            return None

        try:
            find = self._db.find_user_by_id(id=user_id)
            self._db.update_user(find.id, session_id=None)
            return None

        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """
        function to generate a reset password token
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        token = _generate_uuid()
        self._db.update_user(user.id, token=token)
        return token


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
