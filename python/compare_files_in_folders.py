import sys
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import os

def get_folder_path(window_title, message="Please select a folder"):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    if sys.platform.system() == "Darwin":  # macOS supports the message option
        folder_path = filedialog.askdirectory(title=window_title, message=message)
    else:  # Windows and Linux do not
        folder_path = filedialog.askdirectory(title=window_title)
    return folder_path

def compare_files_in_folders(folder1, folder2):
    files_in_folder1 = {f for f in os.listdir(folder1) if Path(folder1, f).is_file()}
    files_in_folder2 = {f for f in os.listdir(folder2) if Path(folder2, f).is_file()}
    
    shared_names = files_in_folder1.intersection(files_in_folder2)
    unique_to_folder1 = files_in_folder1 - files_in_folder2
    unique_to_folder2 = files_in_folder2 - files_in_folder1

    # Split shared names into size-matched and size-mismatched
    common_files = set()
    mismatched_files = set()
    for file in shared_names:
        if Path(folder1, file).stat().st_size == Path(folder2, file).stat().st_size:
            common_files.add(file)
        else:
            mismatched_files.add(file)

    print(f"Files in both folders with matching size ({len(common_files)}):")
    for file in common_files:
        print(f"  - {file}")

    print(f"\nFiles only in '{folder1}' ({len(unique_to_folder1)}):")
    for file in unique_to_folder1:
        print(f"  - {file}")

    print(f"\nFiles only in '{folder2}' ({len(unique_to_folder2)}):")
    for file in unique_to_folder2:
        print(f"  - {file}")

    if mismatched_files:
        print(f"\nFiles in both folders but with different sizes ({len(mismatched_files)}):")
        for file in mismatched_files:
            print(f"  - {file}")


if __name__ == "__main__":
    folder1 = get_folder_path("Select the first folder", "Please select the folder where incoming files arrive")
    folder2 = get_folder_path("Select the second folder", "Please select the folder to compare against")

    compare_files_in_folders(folder1, folder2)