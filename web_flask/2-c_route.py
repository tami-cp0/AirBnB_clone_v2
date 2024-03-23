#!/usr/bin/python3
"""
Module configures and starts the Flask development server
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    """Return a greeting message when the root URL is accessed."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Return a message specific to HBNB
    when the /hbnb URL is accessed.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Return a message specific to C
    when the /c/<text> URL is accessed.
    """
    text = text.split('_')
    formatted_text = "C " + ' '.join(f"{i}" for i in text)
    return formatted_text


if __name__ == '__main__':
    # Run the Flask application with custom host and port
    app.run(host='0.0.0.0', port=5000)
