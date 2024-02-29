#!/usr/bin/env python3
"""
Flask application
"""
from flask import Flask, abort, jsonify, redirect, request
from flask_cors import CORS, cross_origin
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """
    Flask app that has a single GET route ("/")
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    """
    fucntion that returns a list of all register_user
    """
    try:
        email = request.form["email"]
        password = request.form["password"]
    except ValueError:
        abort(400)

    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": email, "message": "user created"})


@app.route("/sessions", methods=["POST"])
def login():
    """
    function that repond to a login request
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie("session_id", session_id)
            return response
        else:
            abort(401)
    except ValueError:
        abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout():
    """
    function that responds to a logout request
    """
    session_id = request.cookies.get("session_id")

    try:
        user_id = AUTH.get_user_from_session_id(session_id)
        AUTH.destroy_session(user_id)
        return redirect("/")
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
