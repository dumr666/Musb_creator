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

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
print('Argument stevilka 2:', str(sys.argv[1]))

PlaylistLink = str(sys.argv[1])
DestDrive = str(sys.argv[2])

print("Destination drive: ", DestDrive)
print("Playlist link: ", PlaylistLink)