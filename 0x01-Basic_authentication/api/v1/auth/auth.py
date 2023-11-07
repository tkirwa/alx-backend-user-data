#!/usr/bin/env python3

"""
Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to require authorization
        Args:
            path (str): The path of the request
            excluded_paths (List[str]): List of excluded paths
        Returns:
            bool: Always False in this case
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Method to get authorization header
        Args:
            request: The Flask request object
        Returns:
            str: Always None in this case
        """
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
