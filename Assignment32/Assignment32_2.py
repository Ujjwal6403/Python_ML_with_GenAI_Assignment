# Please follow below rules while designing automation script as
# Accept input through command line or through file.
# Display any message in log file instead of console.
# For separate task define separate function.
# For robustness handle every expected exception.
# Perform validations before taking any action.
# Create user defined modules to store the functionality.

# 2. Design automation script which accept directory name and 
# write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory.
# Usage: DirectoryDusplicate.py "Demo

# Demo is name of directory.

import sys
import MarvellousDuplicate


def main():

    if len(sys.argv) != 2:
        print("Usage: DirectoryDuplicate.py DirectoryName")
        return

    dirname = sys.argv[1]

    logfile = open("Log.txt", "w")

    MarvellousDuplicate.find_duplicates(dirname, logfile)

    logfile.close()


if __name__ == "__main__":
    main()