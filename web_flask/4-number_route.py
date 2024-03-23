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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python(text="is cool"):
    """
    Return a message specific to Python
    when the /python/<text> or /python URL is accessed.
    """
    text = text.split('_')
    formatted_text = "Python " + ' '.join(f"{i}" for i in text)
    return formatted_text


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Return a message specific to number
    when the /number URL is accessed.
    """
    return f"{n} is a number"


if __name__ == '__main__':
    # Run the Flask application with custom host and port
    app.run(host='0.0.0.0', port=5000)
