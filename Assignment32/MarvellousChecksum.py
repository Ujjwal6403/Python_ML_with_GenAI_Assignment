import os
import hashlib

def CalculateChecksum(path, blocksize=1024):
    try:
        fd = open(path, "rb")
        hobj = hashlib.md5()

        buffer = fd.read(blocksize)
        while len(buffer) > 0:
            hobj.update(buffer)
            buffer = fd.read(blocksize)

        fd.close()
        return hobj.hexdigest()

    except Exception as e:
        return f"Error calculating checksum: {e}"


def DirectoryChecksum(DirName, LogFile):
    try:
        if not os.path.exists(DirName):
            LogFile.write("Directory does not exist\n")
            return

        if not os.path.isdir(DirName):
            LogFile.write("Given path is not a directory\n")
            return

        for FolderName, SubFolders, FileNames in os.walk(DirName):
            for File in FileNames:
                FilePath = os.path.join(FolderName, File)
                checksum = CalculateChecksum(FilePath)
                LogFile.write(f"{FilePath}  ->  {checksum}\n")

    except Exception as e:
        LogFile.write(f"Error scanning directory: {e}\n")