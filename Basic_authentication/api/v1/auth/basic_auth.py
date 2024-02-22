#!/usr/bin/env python3
"""
Basic auth module
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic auth class to manage the API authentication
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        function to extract the base64 encoded authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        encoded = authorization_header.split(" ", 1)[1]

        return encoded
