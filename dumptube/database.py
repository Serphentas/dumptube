from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine('sqlite:///' + os.getcwd() + '/db.sqlite')    
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

def init_db():
    """
    Setting up the database
    """
    Base.metadata.create_all(engine)

