#!/usr/bin/env python3
"""
class to manage the API authentication
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        checks if the user is authorized to access the path
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        handler to get the authorization header
        """
        if (request is None):
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Validates the current user
        """
        return None
