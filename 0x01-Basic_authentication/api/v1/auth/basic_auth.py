#!/usr/bin/env python3
"""Class for handler authorization functions"""

from api.v1.auth.auth import Auth
from typing import TypeVar
import base64

from models.user import User


class BasicAuth(Auth):
    """Class for handler authorization functions"""

    def extract_base64_authorization_header(
            self,
            authorization_header: str
    ) -> str:
        """
        Function that returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        prefix = 'Basic '
        if not authorization_header \
           or not isinstance(authorization_header, str) \
           or not authorization_header.startswith(prefix):
            return None

        return authorization_header.replace(prefix, '')

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
    ) -> str:
        """Function that returns the decoded value of a Base64 string"""
        if not base64_authorization_header or \
           not isinstance(base64_authorization_header, str):
            return None

        try:
            return base64.b64decode(base64_authorization_header)\
                .decode('UTF-8')
        except Exception as _:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Function that returns the user email and password
        from the Base64 decoded value
        """
        if not decoded_base64_authorization_header or \
           not isinstance(decoded_base64_authorization_header, str) or \
           ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(':', 1)

        return credentials[0], credentials[1]

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
    ) -> TypeVar('User'):
        """
        Function that returns the User instance based on
        his email and password
        """
        if not user_email or \
           not isinstance(user_email, str) or \
           not user_pwd or \
           not isinstance(user_pwd, str):
            return None

        user = User()
        users = user.search({'email': user_email})
        if len(users) < 1:
            return None

        user: User = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Function that overloads Auth and retrieves the User
        instance for a request
        """
        authorization = self.authorization_header(request)
        b64 = self.extract_base64_authorization_header(authorization)
        decode_b64 = self.decode_base64_authorization_header(b64)
        cred = self.extract_user_credentials(decode_b64)
        return self.user_object_from_credentials(cred[0], cred[1])
