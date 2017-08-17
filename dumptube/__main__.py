# -*- coding: utf-8 -*-
from fileutils import chk_path, chk_targets
from colors import bcolors
from messaging import fail
import os
import argparse
from download import download

__title__ = 'dumptube'
__version__ = '1.0.0'

def main():
    parser = argparse.ArgumentParser(description='Bulk YouTube downloader')
    parser.add_argument(
        '--dir',
        '-d',
        dest='dumpdir',
        help='Path to download directory'
    )
    args = parser.parse_args()

    # greeting user
    print(bcolors.HEADER + __title__ + " " + __version__ + bcolors.ENDC)

    # checking if target channels and YouTube API key are provided
    if not chk_targets():
        fail("No target file exists, please check the README for more information")
    elif not os.environ.get('YT_API_KEY'):
        fail("No YouTube API key has been set, please check the README for more information")
    else:
        download(args)

if __name__ == '__main__':
    main()
