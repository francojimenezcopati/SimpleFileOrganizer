import os, shutil

def createOrganizer(path:str ,folderName:str, fileTypes:str, pathToOrganize:str=None) -> None:
    """Create a folder, where all the files from the specified extensions are organized.\n
    If the organizer already exists, it organize the files, otherwise,
    it creates the organizer and organize the files.

    Args:
        path (str): The path where the organizer will be created.
        folderName (str): Name of the folder to be created.
        fileTypes (str): extensions of the files to be stored in the folder, 
        separated by '|' (pipe), and with the following format: ".{extension}"
        example: ".jpg|.png|.jpeg".
        pathToOrganize (str): Optional, to organize a different path.
    """
    fullFolderPath = f"{path}\{folderName}"
    if(not pathToOrganize): # If no path to organize was given, organize the path of the folder
        pathToOrganize = path
	
    if(not os.path.isdir(fullFolderPath)): # If the folder doesnt exists, then its created
        os.mkdir(fullFolderPath)
    
    
    fileList = os.listdir(pathToOrganize) # All the files in the path to be organized
    
    extensions = fileTypes.split("|") # the extensions in a list form
    
    print()
    print("Loop through the files into the given path and move the ones that match the extensions.")
    for f in fileList:
        for extension in extensions:
            if(extension in f):
                print(f"Match found.")
                filePath = f"{pathToOrganize}\{f}"
                shutil.move(filePath, fullFolderPath)
    print()

d = "Downloaded_"
path = "D:\DESCARGAS"

images = [path, f"{d}Images", ".jpg|.jpeg|.png"]
docs = [path, f"{d}Docs", ".docx"]
pdfs = [path, f"{d}PDFs", ".pdf"]
videos = [path, f"{d}Videos", ".mp4|.mkv|.wav|.gif|.flac"]
txts = [path, f"{d}TXTs", ".txt"]
excels = [path, f"{d}Excels", ".csv"]
executables = [path, f"{d}Executables", ".exe|.jar"]
rars = [path, f"{d}Rars", ".rar|.7z|.zip"]
mp3s = [path, f"{d}MP3s", ".mp3"]


# ----------------  FOR ORGANIZE ALL OF ABOVE ORGANIZERS AT ONCE  -----------------------
# fullListOfTypes = [images, docs, pdfs, videos, txts, excels, executables, rars, mp3s]
# for type in fullListOfTypes:
#     createOrganizer(*type)
# ---------------------------------------------------------------------------------------


# ----------------  FOR ORGANIZE ONE TYPE AT A TIME  -----------------------
# organizeOrganizer = images
# createOrganizer(*organizeOrganizer)
# --------------------------------------------------------------------------