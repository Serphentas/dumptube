# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Channel(Base):
    """Represents a YouTube channel"""
    __tablename__ = 'channels'
    id = Column(Integer, primary_key=True)
    ytid = Column(String)
    username = Column(String)
    name = Column(String)
    videos = relationship(
        "Video",
        back_populates='channel'
    )

    def __init__(self, ytid, username, name):
        self.ytid = ytid
        self.username = username
        self.name = name

    def __repr__(self):
        return "<Channel(%s, %s, %s)>" % (self.ytid, self.username, self.name)
