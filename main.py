from ftplib import FTP
import os
from dotenv import load_dotenv

# Read env file
load_dotenv()

# Setup global variables
backupRegistry = "backupstore.txt"
minecraftWorldName = os.getenv('MINECRAFT_WORLD_NAME')
localBackupDirectory = os.getenv('OUTPUT_DIRECTORY').rstrip("/") + "/"
localBackupRegistryPath = localBackupDirectory + backupRegistry


def getFile(ftp, fromFilename, toPath):
    """Get a file from a ftp connexion
    fromFilename (String) the source filename
    toPath (String) the destination path (directory and filename)
    """
    print("Begin to copy file " + fromFilename)
    try:
        ftp.retrbinary("RETR " + fromFilename, open(toPath, 'wb').write)
        print("Copied file " + fromFilename)
    except:
        print("Can't/cancelled copying file " + fromFilename)


# Open the FTP connexion
with FTP() as ftp:
    ftp.connect(host=os.getenv('FTP_HOST'), port=int(os.getenv('FTP_PORT')))
    ftp.login(user=os.getenv('FTP_USER'), passwd=os.getenv('FTP_PASSWORD'))
    
    # Get backup registry
    print("Go to backupstore directory")
    ftp.cwd('/backups/' + minecraftWorldName)
    getFile(ftp, backupRegistry, localBackupRegistryPath)

    # Search which backup.zip we need to download
    with open(localBackupRegistryPath, "r") as f:
        lines=[l.rstrip() for l in f.readlines() if len(l) > 0]
        if len(lines) == 0:
            raise Exception("The backupstore.txt file is empty")
        lastLine=lines[-1]
        filenameToFetch="Backup-%s-%s-%s-%s--%s-%s.zip" % (
            (minecraftWorldName,) + tuple(lastLine.split("=")[1:]))
        pathToFile="%s/%s/%s" % tuple(lastLine.split("=")[1:4])

    # Download the backup file
    print("Go to backup directory")
    ftp.cwd('/backups/' + minecraftWorldName + '/' + pathToFile)
    getFile(ftp, filenameToFetch, localBackupDirectory + filenameToFetch)
    ftp.quit()
