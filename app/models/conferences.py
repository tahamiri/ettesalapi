from sqlalchemy import Column, String, Integer

from ..database import Base


class Conference(Base):
    __tablename__ = "conferences"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    Capacity = Column(Integer)
    items = Column(String)

    def __repr__(self):
        return "<User(title='%s')>" % (
            self.title,
        )


