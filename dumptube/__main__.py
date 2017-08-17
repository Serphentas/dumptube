# -*- coding: utf-8 -*-
from fileutils import chk_path, chk_targets
from colors import bcolors
from messaging import fail
import os

__title__ = 'dumptube'
__version__ = '1.0.0'

def main():

    # greeting user
    print(bcolors.HEADER + __title__ + " " + __version__ + bcolors.ENDC)

    # creating dump folder if not existing
    chk_path(os.getcwd() + '/dumps')

    # checking if target channels and YouTube API key are provided
    if not chk_targets():
        fail("No target file exists, please check the README for more information")
    elif not os.environ.get('YT_API_KEY'):
        fail("No YouTube API key has been set, please check the README for more information")
    else:
        import download 

if __name__ == '__main__':
    main()
