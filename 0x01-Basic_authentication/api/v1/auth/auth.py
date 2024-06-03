#!/usr/bin/env python3
"""
Task 3. Auth class

The API authentication class.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth

    The API authentication class manager.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """authorization_header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user
        """
        return None
