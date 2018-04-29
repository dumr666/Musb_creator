# Music USB creator for your autoradio
# Author: Dumr666
# Usage:
# python musb_creator.py <link to playlist> <destination drive>
# must use m3u playlist

#imports
import sys
import os
import shutil
# ID3 import
from tinytag import TinyTag

# Class for track
class track():
    def __init__(self, artist, title, path, length):
        self.artist = artist
        self.title = title
        self.length = length
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
    song=track(None,None,None,None)

    for line in m3ufile:
        line=line.strip()
        if line.startswith('#EXTINF:'):
            # pull length and title from #EXTINF line
            length,song_full=line.split('#EXTINF:')[1].split(',',1)
            artist, title = song_full.split('-')
            artist = artist.rstrip()
            title = title.rstrip()
            song=track(artist,title,None,length)
        elif (len(line) != 0):
            # pull song path from all other, non-blank lines
            song_path = line.replace("/","\\")
            song.path=song_path            
            tracklist.append(song)
            song=track(None,None,None,None)

    m3ufile.close()

    return tracklist

# Get script arguments 
ScriptPath = str(sys.argv[0])
PlaylistLink = str(sys.argv[1])
DestDrive = str(sys.argv[2])

# Print out paths
print("Script path: ", ScriptPath)
print("Destination drive: ", DestDrive)
print("Playlist link: ", PlaylistLink)
tracklist = parsem3u(PlaylistLink)

# Loop in tracklist
for track in tracklist:
    print(track.artist, track.title, track.length, " -- ", track.path)
    usb_folder = DestDrive + track.artist
    if not os.path.isdir(usb_folder):
        print("Kreiranje mape na usbju: ", usb_folder)
        os.makedirs(usb_folder)
        print("Home directory %s was created." %usb_folder)
    
    # Copy mp3 to destination folder
    print("kopiranje v mapo ", track.artist, track.title)
    shutil.copy2(track.path, usb_folder)