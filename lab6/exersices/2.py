import os

a = input()

def check_path(path):
    if os.path.exists(path):
        print("Path exists.")
        if os.access(path, os.R_OK):
            print("Path is readable")
        else:
            print("Path is unreadable")
        if os.access(path, os.W_OK):
            print("Path is writable")
        else:
            print("Path is not writable")  
        if os.access(path, os.X_OK):
            print("Path is executable")
        else:
            print("Path is unexecutable")  
    else:
        print("Path does not exist.")
     

check_path(a)  
