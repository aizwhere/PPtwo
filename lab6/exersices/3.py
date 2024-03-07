import os

def check_path(path):
    if os.path.exists(path):
        
        
        directory_portion, filename = os.path.split(path)
        print( filename)
        print(directory_portion)
    else:
        print("Path does not exist.")

path = input()

check_path(path)