# Please add below features in our project named as Platform Surveillance System
# 1. Add Thread Monitoring Feature
# For each running process, display:
# Process Name
# PID
# Number of Threads created by that process
# Requirement
# Store information in log file along with timestamp

import psutil
import sys
import os
import time
import schedule

############################################################

def CreateLog(FolderName):
    Border = "-"*50

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        print("Directory for log files gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log" % timestamp)

    print("Log file gets created with name : ", FileName)

    fobj = open(FileName, "w")

    fobj.write(Border+"\n")
    fobj.write("---- Marvellous Platform Surveillance System -----\n")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    ########################################################
    # CPU
    fobj.write("CPU Usage : %s %%\n" % psutil.cpu_percent())
    fobj.write(Border+"\n")

    ########################################################
    # RAM
    mem = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%\n" % mem.percent)
    fobj.write(Border+"\n")

    ########################################################
    # Disk
    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border+"\n")

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s -> %s %% used\n" % (part.mountpoint, usage.percent))
        except:
            pass

    fobj.write(Border+"\n")

    ########################################################
    # Network
    net = psutil.net_io_counters()
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
    fobj.write("Recv : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")

    ########################################################
    # Process + Thread Monitoring
    Data = ProcessScan()

    fobj.write("\nProcess and Thread Monitoring Report\n")
    fobj.write(Border+"\n")

    for info in Data:
        fobj.write("Timestamp : %s\n" % time.ctime())
        fobj.write("PID : %s\n" % info.get("pid"))
        fobj.write("Name : %s\n" % info.get("name"))
        fobj.write("Username : %s\n" % info.get("username"))
        fobj.write("Status : %s\n" % info.get("status"))
        fobj.write("Start time : %s\n" % info.get("create_time"))
        fobj.write("CPU %% : %.2f\n" % info.get("cpu_percent"))
        fobj.write("Memory %% : %.2f\n" % info.get("memory_percent"))

        # 🔥 Thread Monitoring Feature
        fobj.write("Number of Threads : %s\n" % info.get("num_threads"))

        fobj.write(Border+"\n")

    fobj.write("----------------- End of Log File ----------------\n")
    fobj.write(Border+"\n")

    fobj.close()

############################################################

def ProcessScan():
    print("Process Scan Report")
    listProcess = []

    # Warm up CPU calculation
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(1)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name", "username", "status", "create_time"])

            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S",
                                                    time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"

            info["cpu_percent"] = proc.cpu_percent()
            info["memory_percent"] = proc.memory_percent()

            # 🔥 Added Thread Count
            info["num_threads"] = proc.num_threads()

            listProcess.append(info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listProcess

############################################################

def main():

    Border = "-"*50
    print(Border)
    print("---- Marvellous Platform Surveillance System -----")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to : ")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Store information about processes")
            print("4 : Store information about CPU")
            print("5 : Store information about RAM usage")
            print("6 : Store information about Disk")
            print("7 : Store information about Threads (New Feature)")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval DirectoryName")

        else:
            print("Invalid option")

    elif(len(sys.argv) == 3):

        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print("Platform Surveillance System started successfully")
        print("Press Ctrl + C to stop the execution")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)

############################################################

if __name__ == "__main__":
    main()