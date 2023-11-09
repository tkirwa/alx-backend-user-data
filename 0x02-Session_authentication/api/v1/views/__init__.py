#!/usr/bin/env python3
""" api/v1/views/__init__.py
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *

User.load_from_file()


from api.v1.views import session_auth
