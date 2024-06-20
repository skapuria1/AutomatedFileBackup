# Automated File Backup
This Python script automates the process of copying a folder from a source directory to a destination directory daily at a specified time. The copied folder is saved in the destination directory with the current date as its name.

## Features
Automatically copies a folder from the source directory to the destination directory every day.
Names the destination folder with the current date.
Handles existing destination folders gracefully.
## Requirements
- Python 3.x
## Installation
- Ensure Python 3 is installed on your system. Download it from the official Python website.
## Usage
1. Save the script as automated_backup.py.
2. Run the script:

`python automated_backup.py`


## Code Explanation
**Imports**

`import os`
`import shutil`
`import datetime`
`import schedule`
`import time`
**os, shutil, datetime, schedule, and time** are standard Python libraries used for file operations, scheduling, and time management.

## User Input

`source_dir = input("Enter source directory: ").replace("\\", "/")`
`destination_dir = input("Enter destination directory: ").replace("\\", "/")`
- Prompts user for directories and normalizes the path separators.
## Backup Function

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")
- Copies the folder from source to dest with today's date as the folder name.
- Handles the case where the folder already exists.
## Scheduling

`schedule.every().day.at("12:30").do(lambda: copy_folder_to_directory(source_dir, destination_dir))`
`copy_folder_to_directory(source_dir, destination_dir)`
- Schedules the backup function to run daily at 12:30 PM.
- Runs the function immediately upon starting the script.
## Main Loop

while True:
    schedule.run_pending()
    time.sleep(60)
- Keeps the script running, checking every minute for scheduled tasks.