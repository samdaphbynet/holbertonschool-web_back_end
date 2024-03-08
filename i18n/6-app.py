#!/usr/bin/env python3
"""
Basic Babel setup
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Config class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("6-app.Config")


@app.route("/")
def index():
    """
    function that render index.html template
    """
    return render_template("6-index.html")


# @babel.localeselector
def get_locale():
    """
    Get the current locale
    """
    locale_param = request.args.get("locale")

    if locale_param and locale_param in app.config["LANGUAGES"]:
        return locale_param
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


def get_user(user_id) -> Union[dict, None]:
    """
    function that get user by user_id
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    function that check if user is logged in
    """
    user_id = request.args.get("login_as")
    if user_id:
        user = get_user(int(user_id))
        if user:
            g.user = user
        else:
            g.user = None
    else:
        g.user = None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
