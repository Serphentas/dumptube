# -*- coding: utf-8 -*-
from database import session
from channel import Channel
from video import Video
import sys

def show_db():
    """Shows all stored channels and all their respective videos"""
    channels = session.query(Channel).all()
    
    for channel in channels:
        sys.stdout.write("* Channel " + str(channel.id) + " ")
        sys.stdout.flush()
        print unicode(channel)
        videos = channel.videos
        
        for video in videos:
            sys.stdout.write("   * Video " + str(video.id) + " ")
            sys.stdout.flush()
            print unicode(video)

