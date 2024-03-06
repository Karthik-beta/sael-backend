import subprocess
import os
import time

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def clear_cache():
    try:
        # Clear Python bytecode files
        command = "del /q /s /f %temp%\\*.pyc"
        subprocess.call(command, shell=True)

        # Clear Django cache
        target_directory = r"C:\GETINSOLUTION\V2\sael-backend"
        os.chdir(target_directory)
        python_exe_path = r"C:\Users\Dell\AppData\Local\Programs\Python\Python311\python.exe"
        command_to_run = f'{python_exe_path} manage.py clear_cache'
        output, error = run_command(command_to_run)
        print("Output (Clear Cache):", output.decode("utf-8"))
        print("Error (Clear Cache):", error.decode("utf-8"))
    except Exception as e:
        print(f"Error clearing cache: {e}")

def main():
    while True:
        try:
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

            # Clear cache
            clear_cache()

            # Wait for 1 minute before running the commands again
            time.sleep(60)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()