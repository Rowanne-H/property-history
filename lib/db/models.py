from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///property_history.db')

Base = declarative_base()

class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer(), primary_key=True)
    
    properties = relationship('Property', backref='owner')

    def __repr__(self):
        return f'Owner(id={self.id})'
    
class Agent(Base):
    __tablename__ = 'agents'

    id = Column(Integer(), primary_key=True)

    properties = relationship('Property', backref='agent')

    def __repr__(self):
        return f'Agent(id={self.id})'
    
class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer(), primary_key=True)
    owner_id = Column(Integer(), ForeignKey('owners.id'))
    agent_id = Column(Integer(), ForeignKey('agents.id'))

    def __repr__(self):
        return f'Property(id={self.id})'

