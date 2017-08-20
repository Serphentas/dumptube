# -*- coding: utf-8 -*-
from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Video(Base):
    """Represents a YouTube video"""
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    ytid = Column(String)
    title = Column(String)
    description = Column(String)
    date = Column(DateTime)
    channel_id = Column(
        Integer,
        ForeignKey('channels.id')
    )
    channel = relationship(
        "Channel",
        back_populates='videos'
    )

    def __init__(self, ytid, title, description, date):
        self.ytid = ytid
        self.title = title
        self.description = description
        self.date = date

    def __repr__(self):
        return "<Video('%s', '%s', '%s')>" % (self.ytid, self.title, self.date)

