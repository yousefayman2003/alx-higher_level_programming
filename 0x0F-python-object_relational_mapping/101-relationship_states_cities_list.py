#!/usr/bin/python3
"""Module that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa"""
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

    # query all states
    states = session.query(State).order_by(State.id).all()

    # print each state and its cities
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    # close session
    session.close()
