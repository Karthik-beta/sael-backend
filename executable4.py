import subprocess
import os
import schedule
import time
import pygetwindow as gw

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def job():
    # Step 1: Navigate to the specified directory
    target_directory = r"C:\GETINSOLUTION\V2\sael-backend"
    os.chdir(target_directory)

    # Step 2: Run the specified commands
    python_exe_path = r"C:\Users\Dell\AppData\Local\Programs\Python\Python311\python.exe"
    
    # Command 1
    command1 = f'{python_exe_path} manage.py import3 "C:\\Users\\Dell\\Desktop\\WIP\\today_shift_target.xlsx"'
    output1, error1 = run_command(command1)
    print("Output for Command 1:", output1.decode("utf-8"))
    print("Error for Command 1:", error1.decode("utf-8"))

    # Command 2
    command2 = f'{python_exe_path} manage.py import_weekly "C:\\Users\\Dell\\Desktop\\WIP\\weekly_target.xlsx"'
    output2, error2 = run_command(command2)
    print("Output for Command 2:", output2.decode("utf-8"))
    print("Error for Command 2:", error2.decode("utf-8"))

    # Command 3
    command3 = f'{python_exe_path} manage.py monthly "C:\\Users\\Dell\\Desktop\\WIP\\monthly_target.xlsx"'
    output3, error3 = run_command(command3)
    print("Output for Command 3:", output3.decode("utf-8"))
    print("Error for Command 3:", error3.decode("utf-8"))

    # Hide the console window
    console = gw.getWindowsWithTitle('Console')[0]
    console.minimize()

def clear_cache():
    # Clear cache logic goes here
    print("Cache cleared.")

def main():
    # Schedule job to run every minute
    schedule.every(1).minutes.do(job)

    # Schedule cache clearing every 10 minutes
    schedule.every(10).minutes.do(clear_cache)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
