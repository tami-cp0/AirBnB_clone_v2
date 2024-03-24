#!/usr/bin/python3
"""Module for configuring and starting the Flask Web application"""
import os
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Return a html page specific to hbnb
    when the /hbnb_filters URL is accessed.
    """
    states = storage.all(State)
    amenity = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states, amenity=amenity)


@app.teardown_appcontext
def teardown(exception):
    """
    Closes current database session
    """
    storage.close()


if __name__ == '__main__':
    # Run the Flask application with custom host and port
    app.run(host='0.0.0.0', port=5000)
