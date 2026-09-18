# os lets Python read environment variables such as databse url
import os

# create_engine creates the connection between python and postgresql
from sqlalchemy import create_engine

# Gets the postgresql connection address from the environment
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://maps_weather:changeme@localhost:5432/maps_weather",
)

# Creates the database engine used by the backend to communicate with postgresql
engine = create_engine(DATABASE_URL)

# text lets sqlalchemy execute a simple SQL statement
from sqlalchemy import text

# DeclarativeBase provides the base class for future database models
from sqlalchemy.orm import DeclarativeBase


# Tests whether the backend can successfully communicate with postgresql
def test_database_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return result.scalar()

# Base is the parent class that future database models will inherit from
class Base(DeclarativeBase):
    pass