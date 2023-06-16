#!/usr/bin/python3
"""Query using sqlalchemy from database"""
import sys
import sqlalchemy
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for states, cities in session.query(State, City).\
            filter(State.id == City.state_id).order_by(City.id):
        print("{}: ({}) {}".format(states.name, cities.id, cities. name))
