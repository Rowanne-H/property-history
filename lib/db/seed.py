#!/usr/bin/env python3

from random import choice as rc

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Owner, Agent, Property

engine = create_engine('sqlite:///property_history.db')
Session = sessionmaker(bind=engine)
session = Session()

def create_owners():
    owners = [Owner() for i in range(500)]
    session.add_all(owners)
    session.commit()
    return owners

if __name__ == '__main__':
    owners = create_owners()