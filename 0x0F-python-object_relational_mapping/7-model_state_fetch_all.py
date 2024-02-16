#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine("""mysql+mysqldb://{}:{}@localhost:3306/{}"""
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    session = sessionmaker(bind=engine)
    states = session().query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
