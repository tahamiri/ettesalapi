from sqlalchemy import Column, String
from ..database import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True)
    password = Column(String)

    def __repr__(self):
        return "<User(username='%s')>" % (
            self.username,
        )

