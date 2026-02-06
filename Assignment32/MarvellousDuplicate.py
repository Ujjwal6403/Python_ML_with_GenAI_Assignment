import os
import hashlib


def calculate_checksum(path):
    hobj = hashlib.md5()

    with open(path, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            hobj.update(data)

    return hobj.hexdigest()


def find_duplicates(dirname, logfile):

    if not os.path.exists(dirname):
        logfile.write("Directory does not exist\n")
        return

    if not os.path.isdir(dirname):
        logfile.write("Given path is not a directory\n")
        return

    checksum_set = set()
    duplicate_files = []

    for folder, subfolder, files in os.walk(dirname):
        for file in files:
            filepath = os.path.join(folder, file)

            try:
                checksum = calculate_checksum(filepath)

                if checksum in checksum_set:
                    duplicate_files.append(filepath)
                else:
                    checksum_set.add(checksum)

            except Exception:
                logfile.write("Error reading file: " + filepath + "\n")

    if len(duplicate_files) > 0:
        logfile.write("Duplicate Files:\n\n")
        for file in duplicate_files:
            logfile.write(file + "\n")
    else:
        logfile.write("No duplicate files found.\n")