# -*- coding: utf-8 -*-
from apiclient.discovery import build
from oauth2client.tools import argparser
import os
from video import Video
from channel import Channel

# creating YouTube API object
YT_API_SERVICE_NAME = "youtube"
YT_API_VERSION = "v3"
yt = build(
    YT_API_SERVICE_NAME,
    YT_API_VERSION,
    developerKey=os.environ.get('YT_API_KEY')
)

def get_videos(channel_id):
  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = yt.search().list(
    channelId=channel_id,
    part="id,snippet",
    order="date",
    maxResults=50
  ).execute()

  videos = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append(Video(
        search_result["id"]["videoId"],
        search_result["snippet"]["title"],
        search_result["snippet"]["description"],
        search_result["snippet"]["publishedAt"]
      ))

  return videos

def find_channel(channel_name):
    search_response = yt.search().list(
        q=channel_name,
        part="id,snippet",
        maxResults=50
    ).execute()

    channels=[]

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#channel":
            channels.append(Channel(
                search_result["id"]["channelId"],
                search_result["snippet"]["title"]
            ))

    return channels
