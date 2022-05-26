#!/usr/bin/env python3
"""
Class that inherits from Auth for creating a
new authentication mechanism
"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Class that inherits from Auth for creating a
    new authentication mechanism
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Function that creates a Session ID for a user_id"""
        if not user_id or \
           not isinstance(user_id, str):
            return None

        session_id = uuid.uuid4().__str__()
        self.user_id_by_session_id[session_id] = user_id
        return session_id
