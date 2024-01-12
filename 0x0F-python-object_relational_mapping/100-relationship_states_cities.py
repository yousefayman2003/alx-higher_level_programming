#!/usr/bin/python3
"""Module that creates the State “California”
    with the City “San Francisco” from the database hbtn_0e_100_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    # create engine and bind it to base
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(engine)
    session = Session()

    # add state and city
    session.add(State(name="California", cities=[City(name="San Francisco")]))

    # commit changes
    session.commit()

    # close session
    session.close()
