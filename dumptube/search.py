# -*- coding: utf-8 -*-
from apiclient.discovery import build
from oauth2client.tools import argparser
import os
import datetime as dt
from video import Video
from channel import Channel

def setup():
    """
    Creating YouTube API object
    """
    YT_API_SERVICE_NAME = "youtube"
    YT_API_VERSION = "v3"
    yt = build(
        YT_API_SERVICE_NAME,
        YT_API_VERSION,
        developerKey=os.environ.get('YT_API_KEY')
    )

def get_videos(channel_id, date):
    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = yt.search().list(
        channelId=channel_id,
        part="id,snippet",
        order="date",
        maxResults=50,
        publishedBefore=date,
        publishedAfter=dt.datetime.strptime('2000-01-01T00:00:00.0', '%Y-%m-%dT%H:%M:%S.%f').isoformat('T') + 'Z'
    ).execute()

    videos = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            if search_result["snippet"]["liveBroadcastContent"] not in ["upcoming", "live"]:
                videos.append(Video(
                    search_result["id"]["videoId"],
                    search_result["snippet"]["title"],
                    search_result["snippet"]["description"],
                    dt.datetime.strptime(search_result["snippet"]["publishedAt"][:-1], '%Y-%m-%dT%H:%M:%S.%f')
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
                channel_name,
                search_result["snippet"]["title"]
            ))

    return channels

