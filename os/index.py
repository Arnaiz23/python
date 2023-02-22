import os

cwd = os.getcwd()
print("Current working directory", cwd)

# Function to get the current working directory
def current_path(): 
    print("Current working directory before") 
    print(os.getcwd()) 
    print() 

current_path()
