from flask import Flask, jsonify, request, abort
from api.v1.views import app_views
from models.user import User
from os import getenv
from api.v1.app import auth


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login():
    email = request.form.get("email")
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400

    password = request.form.get("password")
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            session_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            response.set_cookie(getenv("SESSION_NAME"), session_id)
            return response

    return jsonify({"error": "wrong password"}), 401
