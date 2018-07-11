from sqlalchemy import Column, String, Integer
from orm.base import Base


class Risk(Base):
    __tablename__ = 'risks'

    id = Column(Integer, primary_key=True)
    lob = Column(String)
    name = Column(String)

    def __init__(self, name, lob):
        self.lob = lob
        self.name = name