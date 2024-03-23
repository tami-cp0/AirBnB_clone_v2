#!/usr/bin/python3
from models import storage
from models.state import State

all_states = storage.all(State)
for state_id, state in all_states.items():
    for city in getattr(state.__class__, 'cities').__get__(state):
        print("Find the city {} in the state {}".format(city, state))
