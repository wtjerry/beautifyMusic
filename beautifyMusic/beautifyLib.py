import os
import sys
sys.path.append("/usr/local/lib/python3.4/dist-packages/")
from mutagenx.mp3 import EasyMP3 as MP3


def beautifyFileName(path, ending, prefixToRemove, middlePartToRemove, isDryRun):
  allFiles = os.listdir(path)
  musicFiles = list(filter(lambda f: f.endswith(ending), allFiles))

  for file in musicFiles:
    oldFilePath = path + file
    tmpFile = file.replace(prefixToRemove, "", 1)
    newFile = tmpFile.replace(middlePartToRemove, "", 1)
    newFilePath= path + newFile
    print("renaming file '{source}' to '{dest}'".format(source=file, dest=newFile))
    if(not isDryRun):
      os.rename(oldFilePath, newFilePath)


def setArtist(filePath, artist):
  _setAttribute(filePath, "artist", artist)


def setAlbum(filePath, album):
  _setAttribute(filePath, "album", album)


def setTitle(filePath, title):
  _setAttribute(filePath, "title", title)
  

def _setAttribute(filePath, attributeName, attributeValue):
  id3File = MP3(filePath)
  id3File[attributeName] = attributeValue
  id3File.save()
