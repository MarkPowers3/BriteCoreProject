from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm.base import Base


class Option(Base):
    __tablename__ = 'options'

    id = Column(Integer, primary_key=True)
    field_id = Column('field_id', Integer, ForeignKey('fields.id'))
    field = relationship("Field", backref="options")
    val = Column(String)
    text = Column(String)

    def __init__(self, val, text, field):
        self.val = val
        self.text = text
        self.field = field