#!/usr/bin/env python3

"""
Auth class
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """
    Auth Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to check if authentication is required for a given path.
        Args:
            path (str): The path of the request
            excluded_paths (List[str]): List of excluded paths
        Returns:
            bool: True if authentication is required, False otherwise
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Method to get authorization header
        Args:
            request: The Flask request object
        Returns:
            str: The value of the header request 'Authorization' or None
        """
        if request is not None:
            return request.headers.get("Authorization", None)
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Method to get current user
        Args:
            request: The Flask request object
        Returns:
            TypeVar('User'): Always None in this case
        """
        return None
