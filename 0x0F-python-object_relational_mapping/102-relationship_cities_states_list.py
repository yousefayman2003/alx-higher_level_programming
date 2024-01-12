#!/usr/bin/python3
"""Module that lists all City objects
    from the database hbtn_0e_101_usa"""
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

    # query all citites
    cities = session.query(City).order_by(City.id).all()

    # print each city and its state
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # close session
    session.close()
