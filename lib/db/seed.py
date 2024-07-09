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

def create_agents():
    agents = [Agent() for i in range(100)]
    session.add_all(agents)
    session.commit()
    return agents

def create_properties():
    properties = [Property() for i in range(600)]
    session.add_all(properties)
    session.commit()
    return properties

def delete_records():
    session.query(Owner).delete()
    session.query(Agent).delete()
    session.query(Property).delete()
    session.commit()

if __name__ == '__main__':
    delete_records()
    owners = create_owners()
    agents = create_agents()
    properties = create_properties()