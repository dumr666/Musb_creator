# Music USB creator for your autoradio
# Author: Dumr666
# Usage:
# python musb_creator.py <link to playlist> <destination drive>
# must use m3u playlist

#imports
import sys
# ID3 import
from tinytag import TinyTag

# Class for track
class track():
    def __init__(self, artist, title, path):
        self.artist = artist
        self.title = title
        self.path = path

