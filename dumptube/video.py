# -*- coding: utf-8 -*-
class Video():
  def __init__(self, id, title, description, date):
    self.id = id
    self.title = title
    self.description = description
    self.date = date

  def __repr__(self):
    return "<Video('%s', '%s', '%s')>" % (self.id, self.title, self.date)
