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

# M3U playlist parser
def parsem3u(m3ufile):
    try:
        assert(type(m3ufile) == '_io.TextIOWrapper')
    except AssertionError:
        m3ufile = open(m3ufile,'r')

    """
        All M3U files start with #EXTM3U.
        If not something is wrong
    """

    line = m3ufile.readline()
    if not line.startswith('#EXTM3U'):
        return
    # initialize playlist variables before reading file
    tracklist=[]
    song=track(None,None,None)

    for line in m3ufile:
        line=line.strip()
        if line.startswith('#EXTINF:'):
            # pull length and title from #EXTINF line
            length,title=line.split('#EXTINF:')[1].split(',',1)
            song=track(length,title,None)
        elif (len(line) != 0):
            # pull song path from all other, non-blank lines
            song.path=line
            tracklist.append(song)
            # reset the song variable so it doesn't use the same EXTINF more than once
            song=track(None,None,None)

    m3ufile.close()

    return tracklist
# Get script arguments 
ScriptPath = str(sys.argv[0])
PlaylistLink = str(sys.argv[1])
DestDrive = str(sys.argv[2])
# Do some magic with file paths
PlaylistLink = PlaylistLink.replace("\\","\\\\")
DestDrive = DestDrive.replace("\\", "\\\\")

testline = "#EXTINF:261,Lamb Of God - Terminally Unique"
length,artistline = testline.split('#EXTINF:')[1].split(',',1)
print("dolzina tracka je: ", length)
artist, song = artistline.split('-')
print("artist: ", artist)
print("song je: ", song)
# Print out paths
print("Script path: ", ScriptPath)
print("Destination drive: ", DestDrive)
print("Playlist link: ", PlaylistLink)
