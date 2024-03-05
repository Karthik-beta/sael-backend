import subprocess
import os
import schedule
import time

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def job():
    # Step 1: Navigate to the specified directory
    target_directory = r"C:\GETINSOLUTION\V2\sael-backend"
    os.chdir(target_directory)

    # Step 2: Run the specified command
    python_exe_path = r"C:\Users\Dell\AppData\Local\Programs\Python\Python311\python.exe"
    command_to_run = f'{python_exe_path} manage.py import3 "C:\\Users\\Dell\\Desktop\\WIP\\today_shift_target.xlsx"'
    
    output, error = run_command(command_to_run)

    # Display the output and error, if any
    print("Output:", output.decode("utf-8"))
    print("Error:", error.decode("utf-8"))

def clear_cache():
    # Clear cache logic goes here
    print("Cache cleared.")

def main():
    # Schedule job to run every minute
    schedule.every(1).minutes.do(job)

    # Schedule cache clearing every hour
    schedule.every().hour.do(clear_cache)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
