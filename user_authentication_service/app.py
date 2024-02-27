#!/usr/bin/env python3
"""
Flask application
"""
from flask import Flask, abort, jsonify, request
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
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": email, "message": "user created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
