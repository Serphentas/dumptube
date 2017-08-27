import xml.etree.ElementTree as ET
import urllib
import subprocess
from pytube import YouTube
import os, sys
import datetime as dt
from video import Video
from channel import Channel
from messaging import warn, fail, info
from colors import bcolors
from fileutils import print_targets, chk_path
from search import find_channel, get_videos
from database import session

def download(args):
    # setting the appropriate path for dumps
    if not args.dumpdir:
        dump_root = os.getcwd() + '/dumps/'
    else:
        dump_root = args.dumpdir if args.dumpdir.endswith('\/') else args.dumpdir + '/'
    chk_path(dump_root)

    info("The following target channels have been found:")
    targets = print_targets()
    for target in targets:
        print(bcolors.OKBLUE + " * " + target + bcolors.ENDC)

    # gettings channel content iteratively
    vid_ctr = 0
    vid_size = 0
    for target in targets:
        channels = find_channel(target)

        if len(channels) == 1:
            info("Processing channel '" + target + "'")

            # recovering existing Channel if possible, else storing a new one
            query = session.query(Channel).filter_by(username=target).first()
            if query is None:
                channel = channels[0]
                session.add(channel)
                session.commit()
            else:
                channel = query

            # getting videos iteratively
            videos = get_videos(channel.ytid, dt.datetime.now().isoformat('T') + 'Z')
            done = False
            while not done:
                new_videos = get_videos(channel.ytid, videos[len(videos)-1].date.isoformat('T') + 'Z')
                done = len(new_videos) == 1 and videos[len(videos)-1].ytid == new_videos[0].ytid
                if not done:
                    videos = videos + new_videos[1:49]

            # setting path for this channel's dump folder
            dump_folder = dump_root + target
            chk_path(dump_folder)

            # saving videos
            for video in videos:
                info("Processing video '" + video.title + "'")
                yt = YouTube("https://www.youtube.com/watch?v=" + video.ytid)
                vid_ext = yt.videos[len(yt.videos)-1].extension
                vid_res = yt.videos[len(yt.videos)-1].resolution

                # checking if video file already exists
                if not os.path.isfile(dump_folder + "/" + video.title + "-" + video.ytid + '.' + vid_ext):
                    sys.stdout.write(bcolors.OKBLUE + "Video not downloaded yet, please wait... ")
                    sys.stdout.flush()

                    # downloading video
                    dl = yt.get(vid_ext, vid_res)
                    filename = dump_folder + '/' + video.title + "-" + video.ytid + '.' + vid_ext
                    dl.download(dump_folder)

                    # updating the database
                    query = session.query(Video).filter_by(ytid=video.ytid).first()
                    if query is None:
                        channel.videos.append(video)
                        session.add(video)
                        session.add(channel)
                        session.commit()

                    # renaming video file to original title and appending YouTube id
                    os.rename(dump_folder + '/' + dl.filename + '.' + vid_ext, filename)

                    # updating stats
                    vid_ctr += 1
                    vid_size += os.path.getsize(filename)

                    print(bcolors.OKGREEN + "done" + bcolors.ENDC)
                    print("")
                else:
                    print(bcolors.OKBLUE + "Video already downloaded, skipping" + bcolors.ENDC)
                    print("")
            info("Finished downloading videos from '" + target + "'")
        else:
            warn("More than one channel has been found with the keyword '" + target + "'")
            warn("Please only enter exact channel names")
    info("Dump completed")
    info("Total videos downloaded: " + str(vid_ctr))
    info("Total download size: " + str(vid_size) + " bytes")

