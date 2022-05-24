#!/usr/bin/env python3
"""Class for handler authorization functions"""

from api.v1.auth.auth import Auth
import base64


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
