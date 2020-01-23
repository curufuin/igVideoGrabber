#!/usr/bin/python

import requests
import re
import wget
import sys


class VideoLinkGrabber:

    def __init__(self):
        self.link = str(sys.argv[1])
        self.links = []
        self.videoRegex = r'\"video\_url\"\:\"(?P<link>.*?)\"'

    def getVideo(self):
        r = requests.get(self.link)
        html = r.text
        matches = re.finditer(self.videoRegex, html)
        for match in matches:
            url = unicode(match.group("link")).replace("\u0026", "&")
            print("\n")
            print(str(url) + "\n")
            wget.download(url)
            print("\n")

vg = VideoLinkGrabber()
vg.getVideo()
