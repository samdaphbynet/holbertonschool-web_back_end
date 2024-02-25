#!/usr/bin/env python3
"""
class to manage the API authentication
"""


from os import getenv
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
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != "/":
            path += "/"
        if excluded_paths[-1] != "/":
            excluded_paths += "/"
        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        handler to get the authorization header
        """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Validates the current user
        """
        return None

    def session_cookie(self, request=None):
        """
        function to get the session cookie value from the request
        """
        if request is None:
            return None

        cookies_name = getenv("SESSION_NAME")

        return request.cookies.get(cookies_name)
