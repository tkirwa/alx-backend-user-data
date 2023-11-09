#!/usr/bin/env python3
"""
This module handles all basic authentication for the API.
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    This class manages Session Authentication. It inherits from the Auth class.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        This method creates a Session ID for a user_id.
        Args:
            user_id (str): The ID of the user
        Returns:
            str: The Session ID
        """
        if user_id is None or type(user_id) != str:
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
