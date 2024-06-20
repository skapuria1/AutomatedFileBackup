import os
import shutil
import datetime
import schedule
import time

source_dir = input("Enter source directory: ").replace("\\","/")
print(source_dir)
destinatation_dir = input("Enter destination directory: ").replace("\\","/")

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")

    except FileExistsError:
        print(f"Folder already exists in: {dest}")

schedule.every().day.at("12:30").do(lambda: copy_folder_to_directory(source_dir,destinatation_dir))
copy_folder_to_directory(source_dir, destinatation_dir)

while True:
    schedule.run_pending()
    time.sleep(60)