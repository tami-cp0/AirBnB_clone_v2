#!/usr/bin/python3
"""
Module configures and starts the Flask development server
"""
from flask import Flask

app = Flask(__name__)


# Define your routes and views...
@app.route("/", strict_slashes=False)
def hello():
    """return a string if / url is accessed"""
    return "Hello HBNB!"


if __name__ == '__main__':
    # Run the Flask application with custom host and port
    app.run(host='0.0.0.0', port=5000)
