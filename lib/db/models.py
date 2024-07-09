from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

engine = create_engine('sqlite:///property_history.db')

Base = declarative_base()

class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer(), primary_key=True)

    def __repr__(self):
        return f'Owner(id={self.id})'

