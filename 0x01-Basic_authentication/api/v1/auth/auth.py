#!/usr/bin/env python3


from flask import request
from typing import List, TypeVar


class Auth:

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None or not excluded_paths:
            return True

        new_path = path[0:len(path) - 1] if path[-1] == '/' else path + '/'

        return path not in excluded_paths and new_path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        if request is None or 'Authorization' not in request.headers:
            return None

        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        return None