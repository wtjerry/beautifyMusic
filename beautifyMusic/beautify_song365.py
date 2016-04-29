#
# arg1 path
# arg2 'dryRun' to not make any changes
#

import sys
import os
from glob import glob
from beautifyLib import beautify
sys.path.append("/usr/local/lib/python3.4/dist-packages/")
from mutagenx.mp3 import EasyMP3 as MP3


def getOnlyFiles(ending):
  files = []
  for f in os.listdir(path):
    potentialFile = os.path.join(path, f)
    if os.path.isfile(potentialFile):
      if any(filter(lambda e: f.endswith(e), ending)):
        files.append(f)
  return files


def extractArtist(f):
  artist = f.split(' - ')[0]
  return artist


def extractTitle(f):
  titleWithSuffix = " - ".join(f.split(" - ")[1:])
  title = titleWithSuffix.split(middlePart)[0]   
  return title


def addArtist(files):
  for f in files:
    artist = extractArtist(f)
    print("adding artist '{artist}' to file '{file}'".format(artist=artist, file=f))
    if(not isDryRun):
      fileWithPath = os.path.join(path, f)
      id3File = MP3(fileWithPath)
      id3File["artist"] = artist
      id3File.save()


def addTitle(files):
  for f in files:
    title = extractTitle(f)
    print("adding title '{title}' to file '{file}'".format(title=title, file=f))
    if(not isDryRun):
      fileWithPath = os.path.join(path, f)
      id3File = MP3(fileWithPath)
      id3File["title"] = title
      id3File.save()


def beautify():
  path = sys.argv[1]
  isDryRun = len(sys.argv) > 2 and sys.argv[2]=="dryRun"
  ending = ".mp3"
  middlePart = "_(song365.cc)"

  filePath = glob(path + "*" + ending)[0]
  f = filePath.split('/')[-1]
  prefix = extractArtist(f) + " - "

  files = getOnlyFiles(ending)
  addArtist(files)
  addTitle(files)
  beautify(path, ending, prefix, middlePart, isDryRun)


