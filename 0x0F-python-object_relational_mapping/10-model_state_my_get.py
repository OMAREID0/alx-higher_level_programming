#!/usr/bin/python3
"""
Start link class to table in database
"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    stateName = sys.argv[4]
    states = session().query(State).filter(State.name == stateName)
    try:
        print(states[0].id)
    except IndexError:
        print("Not found")
