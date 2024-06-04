#!/usr/bin/env python3
"""
Task 6. Basic auth

The BasicAuth class
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth

    An imporved API authentication using the Auth class.
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """extract_base64_authorization_header

        Returns the Base64 part of the authorization header.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if "Basic " not in authorization_header:
            return None
        return authorization_header.split('Basic ', 1)[1]
