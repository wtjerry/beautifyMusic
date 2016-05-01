#
# arg1 path
# arg2 album name
# arg3 'dryRun' to not make any changes
#

import sys
import os
from glob import glob
from .beautifyLib import beautifyFileName
from .beautifyLib import setArtist
from .beautifyLib import setAlbum
from .beautifyLib import setTitle


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


  def addTitle(self, files):
    for f in files:
      title = self.extractTitle(f)
      print("adding title '{title}' to file '{file}'".format(title=title, file=f))
      if(not self.isDryRun):
        fileWithPath = os.path.join(self.path, f)
        setTitle(fileWithPath, title)


  def addArtist(self, files):
    for f in files:
      artist = self.extractArtist(f)
      print("adding artist '{artist}' to file '{file}'".format(artist=artist, file=f))
      if(not self.isDryRun):
        fileWithPath = os.path.join(self.path, f)
        setArtist(fileWithPath, artist)


  def addAlbum(self, files):
    for f in files:
      print("adding album '{album}' to file '{file}'".format(album=self.album, file=f))
      if(not self.isDryRun):
        fileWithPath = os.path.join(self.path, f)
        setAlbum(fileWithPath, self.album)


  def renameFiles(self):
    print(self.path + " " + self.ending)
    filePath = glob(self.path + "*" + self.ending)[0]
    f = filePath.split('/')[-1]
    prefix = self.extractArtist(f) + " - "
    beautifyFileName(self.path, self.ending, prefix, self.middlePart, self.isDryRun)


  def beautify(self):
    if len(sys.argv) < 3:
      raise ValueError("Not enough arguments. Arg1: path, Arg2: album, (Arg3: 'dryRun')")

    self.path = sys.argv[1]
    if (not self.path[-1] == "/"):
      self.path = self.path + "/"
    self.album = sys.argv[2]
    self.isDryRun = len(sys.argv) > 3 and sys.argv[3].lower()=="dryrun"
    self.ending = ".mp3"
    self.middlePart = "_(song365.cc)"

    files = self.getOnlyFiles()
    if (len(files) > 0):
      self.addArtist(files)
      self.addAlbum(files)
      self.addTitle(files)
      self.renameFiles()


