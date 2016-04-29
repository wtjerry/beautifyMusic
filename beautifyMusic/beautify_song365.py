#
# arg1 path
# arg2 'dryRun' to not make any changes
#

import sys
import os
from glob import glob
from .beautifyLib import beautify
sys.path.append("/usr/local/lib/python3.4/dist-packages/")
from mutagenx.mp3 import EasyMP3 as MP3


class beautify_song365(object):
  def getOnlyFiles(self):
    files = []
    for f in os.listdir(self.path):
      potentialFile = os.path.join(self.path, f)
      if os.path.isfile(potentialFile):
        if any(filter(lambda e: f.endswith(e), self.ending)):
          files.append(f)
    return files


  def extractArtist(self, f):
    artist = f.split(' - ')[0]
    return artist


  def extractTitle(self, f):
    titleWithSuffix = " - ".join(f.split(" - ")[1:])
    title = titleWithSuffix.split(self.middlePart)[0]   
    return title


  def addArtist(self, files):
    for f in files:
      artist = self.extractArtist(f)
      print("adding artist '{artist}' to file '{file}'".format(artist=artist, file=f))
      if(not self.isDryRun):
        fileWithPath = os.path.join(self.path, f)
        id3File = MP3(fileWithPath)
        id3File["artist"] = artist
        id3File.save()


  def addTitle(self, files):
    for f in files:
      title = self.extractTitle(f)
      print("adding title '{title}' to file '{file}'".format(title=title, file=f))
      if(not self.isDryRun):
        fileWithPath = os.path.join(self.path, f)
        id3File = MP3(fileWithPath)
        id3File["title"] = title
        id3File.save()


  def beautify(self):
    self.path = sys.argv[1]
    if (not self.path[-1] == "/"):
      self.path = self.path + "/"
    self.isDryRun = len(sys.argv) > 2 and sys.argv[2]=="dryRun"
    self.ending = ".mp3"
    self.middlePart = "_(song365.cc)"

    filePath = glob(self.path + "*" + self.ending)[0]
    f = filePath.split('/')[-1]
    prefix = self.extractArtist(f) + " - "

    files = self.getOnlyFiles()
    self.addArtist(files)
    self.addTitle(files)
    beautify(self.path, self.ending, prefix, self.middlePart, self.isDryRun)


