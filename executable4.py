import subprocess
import os

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def main():
    # Step 1: Navigate to the specified directory
    target_directory = r"C:\GETINSOLUTION\V2\sael-backend"
    os.chdir(target_directory)

    # Step 2: Run the specified commands
    python_exe_path = r"C:\Users\Dell\AppData\Local\Programs\Python\Python311\python.exe"

    # Command 1
    command_to_run = f'{python_exe_path} manage.py import3 "C:\\Users\\Dell\\Desktop\\WIP\\today_shift_target.xlsx"'
    output, error = run_command(command_to_run)
    print("Output (Command 1):", output.decode("utf-8"))
    print("Error (Command 1):", error.decode("utf-8"))

    # Command 2
    command_to_run = f'{python_exe_path} manage.py import_weekly "C:\\Users\\Dell\\Desktop\\WIP\\weekly_target.xlsx"'
    output, error = run_command(command_to_run)
    print("Output (Command 2):", output.decode("utf-8"))
    print("Error (Command 2):", error.decode("utf-8"))

    # Command 3
    command_to_run = f'{python_exe_path} manage.py monthly "C:\\Users\\Dell\\Desktop\\WIP\\monthly_target.xlsx"'
    output, error = run_command(command_to_run)
    print("Output (Command 3):", output.decode("utf-8"))
    print("Error (Command 3):", error.decode("utf-8"))

if __name__ == "__main__":
    main()