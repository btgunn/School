#Automate creation of school folders and copy files from a separate directory
#Benjamin Gunn v1.0
#Python 3.10.9
import os
import shutil

def createFolder(path):
    if(os.path.exists(path)):
        print("folder exists")
    else:
        try:
            os.mkdir(path)
        except FileExistsError:
            print("{0} already exists".format(path))
        except FileNotFoundError:
            print("Parent directory of {0} doesn't exist.".format(path))
        except Exception as e:
            print("Unhandled exception: {0}".format(e))
    return True

#Read list of directories to create from file
if os.path.isfile("folders.txt"):
    with open("folders.txt") as folders:
        folderArray = folders.read().splitlines()
    
    for folder in folderArray:
        createFolder(folder)
else:
    print("folders.txt not found")


#Copy all files from fileSourceDir to the fileDest directory
fileSourceDir = "F:\\tmpSchoolFiles"
fileDestination = "F:\\School\\CurrentSemester\\INFM109\\"

for (path, dirnames, filenames) in os.walk(fileSourceDir):
    for file in filenames:
        tmpSrc = path + "\\" + file
        tmpDest = fileDestination + file
        print("Copying {0} to {1}".format(tmpSrc,tmpDest))
        shutil.copy2(tmpSrc, fileDestination)