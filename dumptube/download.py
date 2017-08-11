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

        videos = get_videos(channel.id)
        dump_folder = os.getcwd() + '/dumps/' + target
        chk_path(dump_folder)

        # saving videos
        for video in videos:
            info("Processing video '" + video.title + "'")
            yt = YouTube("https://www.youtube.com/watch?v=" + video.id)
            vid_ext = yt.videos[len(yt.videos)-1].extension
            vid_res = yt.videos[len(yt.videos)-1].resolution

            # checking if video file already exists
            if not os.path.isfile(dump_folder + "/" + video.title + "-" + video.id + '.' + vid_ext):
                sys.stdout.write(bcolors.OKBLUE + "Video not downloaded yet, please wait... ")
                sys.stdout.flush()

                dl = yt.get(vid_ext, vid_res)
                dl.download(dump_folder)

                # renaming video file to original title and appending YouTube id
                os.rename(dump_folder + '/' + dl.filename + '.' + vid_ext,dump_folder + '/' + video.title + "-" + video.id + '.' + vid_ext)
                print(bcolors.OKGREEN + "done" + bcolors.ENDC)
                print("")
            else:
                print(bcolors.OKBLUE + "Video already downloaded, skipping" + bcolors.ENDC)
                print("")
    else:
        print(bcolors.WARNING + "More than one channel has been found with the keyword '" + channel + "'" + bcolors.ENDC)
        print(bcolors.WARNING + "Please only enter exact channel names" + bcolors.ENDC)
