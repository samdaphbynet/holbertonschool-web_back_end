#!/usr/bin/env python3
"""
Module for the API Session Auth
"""
from api.v1.views import app_views
from os import getenv
from flask import abort, jsonify, request
from models.user import User


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login():
    """
    post request handler for login
    """
    email = request.form.get("email")
    if not email:
        return jsonify({"error": "email is missing"}), 400

    password = request.form.get("password")
    if not password:
        return jsonify({"error": "password is missing"}), 400

    try:
        find_user = User.search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not find_user:
        return jsonify({"error": "no user found for this email"}), 404

    for user in find_user:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    user = find_user[0]
    session_id = auth.create_session(user.id)

    SESSION_NAME = getenv("SESSION_NAME")

    response = jsonify(user.to_json())
    response.set_cookie(SESSION_NAME, session_id)

    return response


@app_views.route("/auth_session/logout", methods=["DELETE"], strict_slashes=False)
def logout():
    """Logout from the session"""
    from api.v1.app import auth

    deleted = auth.destroy_session(request)

    if not deleted:
        abort(404)

    return jsonify({}), 200
