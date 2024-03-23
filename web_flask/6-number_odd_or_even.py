#!/usr/bin/python3
"""
Module configures and starts the Flask development server
"""
from flask import Flask, render_template

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
    when the /number/<int:n> URL is accessed.
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Return a message specific to number_template
    when the /number_template/<int:n> URL is accessed.
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Return a message specific to number_template
    when the /number_template/<int:n> URL is accessed.
    """
    if n % 2 == 0:
        string = "even"
    else:
        string = "odd"
    return render_template('6-number_odd_or_even.html', n=n, string=string)


if __name__ == '__main__':
    # Run the Flask application with custom host and port
    app.run(host='0.0.0.0', port=5000)
