from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm.base import Base


class Field(Base):
    __tablename__ = 'fields'

    id = Column(Integer, primary_key=True)
    risk_id = Column('risk_id', Integer, ForeignKey('risks.id'))
    risk = relationship("Risk", backref="fields")
    uniqueId = Column(String)
    name = Column(String)
    type = Column(String)
    maxLength = Column(Integer)

    def __init__(self, name, uniqueId, type, maxLength, risk):
        self.name = name
        self.uniqueId = uniqueId
        self.type = type
        self.maxLength = maxLength
        self.risk = risk