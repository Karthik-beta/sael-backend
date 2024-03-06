import subprocess
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', line_buffering=True)

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def main():
    # Step 1: Navigate to the specified directory
    target_directory = r"C:\GETINSOLUTION\V2\sael-backend"
    os.chdir(target_directory)

    # Step 2: Run the specified command
    python_exe_path = r"C:\Users\Dell\AppData\Local\Programs\Python\Python311\python.exe"
    command_to_run = f'{python_exe_path} manage.py monthly "C:\\Users\\Dell\\Desktop\\WIP\\monthly_target.xlsx"'
    
    output, error = run_command(command_to_run)

    # Display the output and error, if any
    print("Output:", output.decode("utf-8"))
    print("Error:", error.decode("utf-8"))

if __name__ == "__main__":
    main()
