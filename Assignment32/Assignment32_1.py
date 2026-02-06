# Please follow below rules while designing automation script as
# Accept input through command line or through file.
# Display any message in log file instead of console.
# For separate task define separate function.
# For robustness handle every expected exception.
# Perform validations before taking any action.
# Create user defined modules to store the functionality.

# 1. Design automation script which accept directory name and display checksum of all files.
# Usage: DirectoryChecksum.py "Demof
# Demo is name of directory.

import sys
import time
import MarvellousChecksum

def CreateLogFile():
    try:
        timestamp = time.ctime()
        timestamp = timestamp.replace(" ", "_")
        timestamp = timestamp.replace(":", "_")

        filename = "MarvellousLog%s.log" % timestamp
        fobj = open(filename, "w")
        return fobj

    except Exception as e:
        print("Unable to create log file", e)
        exit()


def main():
    if len(sys.argv) != 2:
        print("Usage: DirectoryChecksum.py DirectoryName")
        exit()

    LogFile = CreateLogFile()

    LogFile.write("----- Directory Checksum Log -----\n")
    LogFile.write("Directory name: " + sys.argv[1] + "\n\n")

    MarvellousChecksum.DirectoryChecksum(sys.argv[1], LogFile)

    LogFile.write("\n----- End of Log -----\n")
    LogFile.close()


if __name__ == "__main__":
    main()