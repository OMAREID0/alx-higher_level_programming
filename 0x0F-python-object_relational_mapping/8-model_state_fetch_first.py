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
    states = session().query(State).order_by(State.id).first()
    if states is None:
        print("Nothing")
    else:
        print("{}: {}".format(states.id, states.name))
