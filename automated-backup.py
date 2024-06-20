import os
import shutil
import datetime
import schedule
import time

source_dir = input("Enter source directory: ").replace("\\","/")    # Get source directory from user input and normalize path
destinatation_dir = input("Enter destination directory: ").replace("\\","/")        # Get destination directory from user input and normalize path

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
     # Create a new destination path with today's date as the folder name
    dest_dir = os.path.join(dest, str(today))

    try:
         # Copy the entire directory tree from source to destination
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")

    except FileExistsError:
        print(f"Folder already exists in: {dest}")

# Schedule the backup function to run every day at 12:30 PM
schedule.every().day.at("12:30").do(lambda: copy_folder_to_directory(source_dir,destinatation_dir))
# Run the backup function immediately upon starting the script
copy_folder_to_directory(source_dir, destinatation_dir)

# Infinite loop to keep the script running and check for scheduled tasks
while True:
    # Run any pending scheduled tasks
    schedule.run_pending()
    # Wait for 60 seconds before checking again
    time.sleep(60)