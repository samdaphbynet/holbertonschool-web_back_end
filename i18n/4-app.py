#!/usr/bin/env python3
"""
Basic Babel setup
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Config class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("4-app.Config")


@app.route("/")
def index():
    """
    function that render index.html template
    """
    return render_template("3-index.html")


# babel.init_app(app, locale_selector=get_locale)
@babel.localeselector
def get_locale():
    """
    Get the current locale
    """

    locale_param = request.args.get("locale")

    if locale_param and locale_param in app.config["LANGUAGES"]:
        return locale_param

    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
