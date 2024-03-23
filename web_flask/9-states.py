#!/usr/bin/python3
"""Module for configuring and starting the Flask Web application"""
import os
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states():
    """
    Return a html page specific to states
    when the /states URL is accessed.
    """
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """
    Return a html page specific to states
    when the /states/<id> URL is accessed.
    """
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """
    Closes current database session
    """
    storage.close()
    
if __name__ == '__main__':
    # Run the Flask application with custom host and port
    app.run(host='0.0.0.0', port=5000)