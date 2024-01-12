#!/usr/bin/python3
"""Module that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa"""
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

    # create and add instance to table
    instance = State(name="Louisiana")
    session.add(instance)

    # commit changes
    session.commit()

    # print instance id
    print(instance.id)

    # close session
    session.close()
