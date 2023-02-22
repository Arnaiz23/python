# List the content of the directory that the user introduces in the input
import os

directory=input("Choose a directory: ")

path=os.path.join("/home/arnaiz/", directory)

def directoryExists(directory):
    return os.path.isdir(directory)

print(f"The actual path is: {path}")

if directoryExists(path):
    answer=input("Do you want to create a folder in this directory??: [Y/n] ")

    if answer.lower() == "y":
        print("Create")
    else:
        print("Don't create")
else:
    print("This directory doesn't exists")


