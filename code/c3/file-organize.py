import os
import shutil

def organize_directory(path):
    for item in os.listdir(path):
        file = os.path.join(path, item)
        if os.path.isfile(file):
            file_ext = item.split('.')[-1]
            new_dir = os.path.join(path, file_ext)
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
            shutil.move(file, os.path.join(new_dir, item))

if __name__ == "__main__":
    directory = input("Please input the directory path: ")
    organize_directory(directory)