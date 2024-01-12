#!/usr/bin/python3
"""Module that deletes all State objects with a name containing
    the letter a from the database hbtn_0e_6_usa"""
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

    # get states containing `a`
    states = session.query(State).filter(State.name.like("%a%")).all()

    # delete states
    for state in states:
        session.delete(state)

    # commit changes
    session.commit()

    # close session
    session.close()
