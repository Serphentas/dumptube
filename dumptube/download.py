import xml.etree.ElementTree as ET
import urllib
import subprocess
from pytube import YouTube
import os, sys, datetime
from video import Video
from channel import Channel
from messaging import warn, fail, info
from colors import bcolors
from fileutils import print_targets, chk_path
from search import find_channel, get_videos

info("The following target channels have been found:")
targets = print_targets()
for target in targets:
    print(bcolors.OKBLUE + " * " + target + bcolors.ENDC)

# gettings channel content iteratively
for target in targets:
    channels = find_channel(target)

    if len(channels) == 1:
        channel = channels[0]
        info("Processing channel '" + channel.username + "'")

        print channel
        videos = get_videos(channel.id)
        
        for video in videos:
            print video
        print videos[len(videos)-1].title
        chk_path('/dumps/' + channel.username)
        


        # saving XML video feed locally
        xml_filename = 'feed_' + channel.username + '-' + str(datetime.date.today()) + '.xml'
        save_feed(channel.username, xml_filename)
        root = get_feed(xml_filename)

        # iterating through feed file
        for child in root:
            # if the current element is a video entry
            if "entry" in child.tag:
                # creating Video and YouTube objects
                video = Video(child[3].text, child[1].text, child[8][3].text, child[7].text)
                yt = YouTube("https://www.youtube.com/watch?v=" + video.id)

                # printing video information    
                print(bcolors.OKGREEN + "Entry found !" + bcolors.ENDC)
                print("Title: " + video.title)
                print("Date: " + video.date)
                print("Description: " + video.description)
                print("URL: https://www.youtube.com/watch?v=" + video.id)

                # checking if video file already exists
                if not os.path.isfile(video.title + "-" + video.id + '.mp4'):
                    sys.stdout.write(bcolors.OKBLUE + "Video not downloaded yet, processing... ")
                    sys.stdout.flush()
                    dl = yt.get('mp4', '720p')
                    dl.download('./dumps/' + channel)

                    # renaming video file to original title and appending YouTube id
                    os.rename(dl.filename + ".mp4", video.title + "-" + video.id + ".mp4")
                    print(bcolors.OKGREEN + "done" + bcolors.ENDC)
                    print("")
                else:
                    print(bcolors.OKBLUE + "Video already downloaded, skipping" + bcolors.ENDC)
            print("")
    else:
        print(bcolors.WARNING + "More than one channel has been found with the keyword '" + channel + "'" + bcolors.ENDC)
        print(bcolors.WARNING + "Please only enter exact channel names" + bcolors.ENDC)

