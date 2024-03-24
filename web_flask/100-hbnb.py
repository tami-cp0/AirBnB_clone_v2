#!/usr/bin/python3
"""Module for configuring and starting the Flask Web application"""
import os
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Return a html page specific to hbnb
    when the /hbnb_filters URL is accessed.
    """
    states = storage.all(State)
    amenity = storage.all(Amenity)
    places = storage.all(Place)
    return render_template('100-hbnb.html', states=states, amenity=amenity, places=places)


@app.teardown_appcontext
def teardown(exception):
    """
    Closes current database session
    """
    storage.close()


if __name__ == '__main__':
    # Run the Flask application with custom host and port
    app.run(host='0.0.0.0', port=5000)
