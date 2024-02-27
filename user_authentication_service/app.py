#!/usr/bin/env python3
"""
Flask application
"""
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """
    Flask app that has a single GET route ("/")
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
