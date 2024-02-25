#!/usr/bin/env python3
"""
class SessionAuth that inherits from class Auth
"""
import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    class to manage the session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        function to create a new session
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        function to get the user id for a session id
        """
        if session_id is None or not isinstance(session_id, str):
            return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return a User ID based on a Session ID."""
        if session_id is None or not isinstance(session_id, str):
            return None

        # Return the value (the User ID) for the key session_id
        return self.user_id_by_session_id.get(session_id)
