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


@app_views.route("/auth_session/logout", methods=["DELETE"],
                 strict_slashes=False)
def logout():
    """
    Deletes the user session / logout.

    Returns:
    dict: An empty dictionary with the status code 200 if the session
      was destroyed.
          Aborts with a 404 error if the session was not destroyed.
    """
    destroyed = auth.destroy_session(request)
    if not destroyed:
        abort(404)

    return jsonify({}), 200
