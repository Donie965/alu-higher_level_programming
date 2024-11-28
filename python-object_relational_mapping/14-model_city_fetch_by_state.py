#!/usr/bin/python3
"""
Prints all City objects from a database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Connect to the MySQL database using the provided arguments
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    
    # Create tables if they do not exist (creates both State and City tables)
    Base.metadata.create_all(eng)
    
    # Create a session to interact with the database
    Session = sessionmaker(bind=eng)
    session = Session()

    # Query to get all City objects and their corresponding State objects
    rows = session.query(City, State).filter(City.state_id == State.id).order_by(City.id).all()
    
    # If there are records, print them in the desired format
    if rows:
        for city, state in rows:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    else:
        print("No cities found.")

    # Close the session
    session.close()
