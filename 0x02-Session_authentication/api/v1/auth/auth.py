#!/usr/bin/env python3
"""
This module handles the authentication for the API.
"""
import os
import re
from typing import List, TypeVar

# from flask import request


class Auth:
    """
    This class manages the authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        This method checks if a path requires authentication.
        Args:
            path (str): The path of the request
            excluded_paths (List[str]): List of excluded paths
        Returns:
            bool: False if the path is in the list of excluded paths,
              True otherwise
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ""
                if exclusion_path[-1] == "*":
                    pattern = "{}.*".format(exclusion_path[0:-1])
                elif exclusion_path[-1] == "/":
                    pattern = "{}/*".format(exclusion_path[0:-1])
                else:
                    pattern = "{}/*".format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        This method retrieves the value of the 'Authorization' header from
          a Flask request object.
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
        This method retrieves the current user.
        Args:
            request: The Flask request object
        Returns:
            TypeVar('User'): Always None in this case
        """
        return None

    def session_cookie(self, request=None) -> str:
        """
        Returns the value of the session cookie from the request.

        This method retrieves the name of the session cookie from the
          environment
        variables and then gets the value of that cookie from the
          request. If the
        request is None or the cookie is not present in the request,
          it returns None.

        Parameters:
        request (Request): The Flask request object from which the cookie
          is to be retrieved.

        Returns:
        str: The value of the session cookie, or None if the request is
          None or the cookie is not present.
        """
        if request is not None:
            cookie_name = os.getenv("SESSION_NAME")
            return request.cookies.get(cookie_name)
