#!/usr/bin/python3
"""Module that lists all State objects from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
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

    # make a query
    results = session.query(State).order_by(State.id)

    # print results
    for state in results:
        print(f"{state.id}: {state.name}")

    # close session
    session.close()
