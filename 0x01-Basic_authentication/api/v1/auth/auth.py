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
        bool: True if path is not in excluded_paths, False otherwise
    """
    if path is None:
        return True

    if excluded_paths is None or len(excluded_paths) == 0:
        return True

    # Add a trailing slash to path if not present for uniformity
    if path[-1] != "/":
        path += "/"

    for exc_path in excluded_paths:
        # If the excluded path ends with '*', check if the start of the path matches
        if exc_path[-1] == "*":
            if path.startswith(exc_path[:-1]):
                return False
        elif path == exc_path:
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
