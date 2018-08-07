from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'sqlite:///app.db'
# create a SQLAlchemy engine
engine = create_engine(db_url)

# create a SQLAlchemy ORM session factory bound to this engine
Session = sessionmaker(bind=engine)

# a base class for our classes definitions
Base = declarative_base()

