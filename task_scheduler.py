
from pathlib import Path
import subprocess
import time
import os

url = "https://exemple.com"
comand = f"wget {url}"
unziping = "unzip main.zip"
directory = "filefolder-main"
execution = "python3 yourfile.py"


file = Path("file.py")
file2 = Path("filefolder-main")

try:
    if not file.is_file():
        print("File not exist. \n")
        time.sleep(1)
        print("Downloading file...\n\n") 
        subprocess.run(comand, shell=True)
        time.sleep(1)
        print("Unziping file.\n")
        subprocess.run(unziping, shell=True)
        time.sleep(1)
        print("Changing directory.")
        os.chdir(directory) 
        print("#Running script.#")
        subprocess.run(execution, shell=True)
    elif file2.is_file():
        print("Changing directory.")
        os.chdir(directory) 
        print("#Running script.#")
        subprocess.run(execution, shell=True)
    else:
        print("Failure to acess file.\n")
