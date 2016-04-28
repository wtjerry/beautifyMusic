import os

def beautify(path, ending, prefixToRemove, middlePartToRemove, isDryRun):
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

