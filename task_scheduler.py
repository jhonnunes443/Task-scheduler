import schedule
import time
import datetime
import subprocess

tasks = [
    {"name": "Task1", "max_runtime": 3, "command": r"python C:\Users\Usuario\Documents\'My files'\'Python projects'\keylogger\keylogger.py"},
    {"name": "Task2", "max_runtime": 6, "command": r"exit()"},
]


def task1_actions():
    try:
        print("Task1: Starting action 1")
        input("Press Enter to continue...")  
    
        print("Task1: Action 1 completed")
        print("Task1: Starting action 2")
        input("Press Enter to continue...") 

        print("Task1: Action 2 completed")
    except Exception as e:
        print(f"Task1: Error executing actions: {str(e)}")
if __name__ == "__main__":
    task1_actions()

def execute_task(task_name, max_runtime, command):
    try:
        start_time = datetime.datetime.now()

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        process.communicate()
        exit_code = process.returncode
        end_time = datetime.datetime.now()
        runtime = (end_time - start_time).total_seconds() / 3600  
        if runtime > max_runtime:
            print(f"Task '{task_name}' exceeded max runtime ({max_runtime} hours) and was terminated.")
            process.terminate()  
        else:
            print(f"Task '{task_name}' completed in {runtime:.2f} hours.")
            if exit_code != 0:
                print(f"Task '{task_name}' encountered an error. Exit code: {exit_code}")
    except Exception as e:
        print(f"Error executing task '{task_name}': {str(e)}")  


for task in tasks:
    schedule.every().minute.do(execute_task, task["name"], task["max_runtime"], task["command"])

while True:
    schedule.run_pending()
    time.sleep(1)  # Check for scheduled tasks every minute
