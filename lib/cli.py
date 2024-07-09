#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db/property_history.db')
Session = sessionmaker(bind=engine)
session = Session()

from db.models import Owner, Agent, Property

if __name__ == '__main__':
    property_id = input("Please enter property id: ")
    
    while property_id:
        if property_id.isdigit():
            if 1 <= int(property_id) <= 500:
                property = session.query(Property).filter(Property.id == property_id)[0] 
                print(f'This property belongs to owner with id {property.owner_id} and is managed by agent with id {property.agent_id}')
                property_id = input("Please enter property id: ")
            else:
                property_id = input("Please enter an integer between 1 and 500: ")
        else:
            property_id = input("Please enter an integer: ")

        
        

    
    
        

    