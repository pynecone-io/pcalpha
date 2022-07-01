"""Database built into Pynecone."""

import sqlmodel

from pynecone import constants
from pynecone.base import Base

sqlite_url = f"sqlite:///{constants.DB_NAME}"
engine = sqlmodel.create_engine(sqlite_url, echo=True)


class Model(Base, sqlmodel.SQLModel):
    """Base class to define a table in the database."""

    # The primary key for the table.
    id: int = sqlmodel.Field(primary_key=True)

    @staticmethod
    def create_all():
        """Create all the tables."""
        sqlmodel.SQLModel.metadata.create_all(engine)

    @classmethod
    @property
    def select(cls):
        """Select rows from the table.

        Returns:
            The select statement.
        """
        return sqlmodel.select(cls)


def session():
    """Get a session to interact with the database.

    Returns:
        A database session.
    """
    return sqlmodel.Session(engine)
