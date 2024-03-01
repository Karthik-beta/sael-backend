import os
import subprocess

# Define the directory path
directory_path = r"C:\GETINSOLUTION\sael-backend"

# Change the current working directory to the specified path
os.chdir(directory_path)

# Define the command to be executed
command = 'python manage.py import3 "C:\\Users\\Dell\\Desktop\\WIP\\today_shift_target.xlsx"'

# Run the command using subprocess
try:
    subprocess.run(command, shell=True, check=True)
    print("Script executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
