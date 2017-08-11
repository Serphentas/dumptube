# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class Channel:
    def __init__(self, id, username):
        self.id = id
        self.username = username

    def __repr__(self):
        return "<Channel(%s, %s)>" % (self.id, self.username)
