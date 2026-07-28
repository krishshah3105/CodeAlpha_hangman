"""Task Automation: Move all .jpg files from one folder to a new folder."""

import os
import shutil


def collect_jpg_files(source_folder):
    jpg_files = []
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            jpg_files.append(filename)
    return jpg_files


def move_files(source_folder, destination_folder, filenames):
    os.makedirs(destination_folder, exist_ok=True)
    moved = []
    for filename in filenames:
        source_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, dest_path)
        moved.append(filename)
    return moved


def main():
    print("JPG File Mover")
    source_folder = input("Enter the source folder path: ").strip()
    destination_folder = input("Enter the destination folder path: ").strip()

    if not source_folder or not destination_folder:
        print("Source and destination folders are required.")
        return

    if not os.path.isdir(source_folder):
        print(f"Source folder does not exist: {source_folder}")
        return

    jpg_files = collect_jpg_files(source_folder)
    if not jpg_files:
        print("No .jpg files found in the source folder.")
        return

    moved_files = move_files(source_folder, destination_folder, jpg_files)
    print(f"Moved {len(moved_files)} .jpg file(s) from '{source_folder}' to '{destination_folder}'.")
    for filename in moved_files:
        print(f"  - {filename}")


if __name__ == "__main__":
    main()
