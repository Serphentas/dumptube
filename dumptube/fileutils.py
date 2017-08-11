import os
import urllib
import xml.etree.ElementTree as ET

def chk_targets():
    return os.path.isfile('targets')

def print_targets():
    return [line.rstrip('\n') for line in open('targets')]

def save_feed(channel_name, xml_filename):
    feed = urllib.URLopener()
    feed.retrieve('https://www.youtube.com/feeds/videos.xml?user=' + channel_name, xml_filename)

def get_feed(xml_filename):
    return ET.parse(xml_filename).getroot()

def chk_path(dir_path):
    dumps_path = os.path.abspath(os.getcwd() + dir_path)
    if not os.path.exists(dumps_path):
        os.makedirs(dumps_path)
