#!/usr/bin/env python3
"""Class to manage the API authentication"""

from typing import List, TypeVar


class Auth:
    """Class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Function that validates excluded paths"""
        if path is None or not excluded_paths:
            return True

        new_path = path[0:len(path) - 1] if path[-1] == '/' else path + '/'

        for e in excluded_paths:
            if e.endswith('*') and new_path.startswith(e[:-1]):
                return False

        return path not in excluded_paths and new_path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Function that validate the Authorization header"""
        if request is None or 'Authorization' not in request.headers:
            return None

        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Function that validates the current logged user"""
        return None
