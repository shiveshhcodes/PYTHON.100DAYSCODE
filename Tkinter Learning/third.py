# import os
# import shutil
# import time


# def ensure_py_extension(filename):
#     if not filename.endswith('.py'):
#         filename += '.py'
#     return filename

# file_names = ["first", "second", "third", "fourth", "fifth"]  # Add more names as needed
# current_index = 0

# while True:
    
#     source_file = input("ENTER SOURCE FILE - ")
#     if source_file.lower()=="quit":
#         break
#     else:
#      pass
#     copy_destination_file = input("ENTER DESTINATION FILE - ")

#     source_file = ensure_py_extension(source_file)
#     copy_destination_file = ensure_py_extension(copy_destination_file)

#     source = f"/Users/shiveshrichhariya/Desktop/GITHUB/100 DAYS OF CODE/PYTHON.100DAYSCODE/Tkinter Learning/{source_file}"
#     destination = f"/Users/shiveshrichhariya/Desktop/GITHUB/100 DAYS OF CODE/PYTHON.100DAYSCODE/Tkinter Learning/{copy_destination_file}"

#     # print(f"Source path: {source}")
#     # print(f"Destination path: {destination}")

#     destination_dir = os.path.dirname(destination)
#     if not os.path.exists(destination_dir):
#         print(f"Creating directory: {destination_dir}")
#         os.makedirs(destination_dir)

#     if os.path.exists(source):
#         # print(f"Copying file from {source} to {destination}")
#         # time.sleep(1.3)
#         print("Processingggggg!! ⏳")
#         shutil.copy(source, destination)
#         # time.sleep(1.34)
#         print("Done Shivesh Boss")
        
#     else:
#      print(f"Source file does not exist , please try again")
#     time.sleep(1)
    
# import os
# import glob

# def ensure_py_extension(filename):
#     if not filename.endswith('.py'):
#         filename += '.py'
#     return filename

# def get_latest_file(directory):
#     list_of_files = glob.glob(os.path.join(directory, '*'))  # Get all files in the directory
#     if not list_of_files:
#         return None
#     latest_file = max(list_of_files, key=os.path.getctime)  # Get the latest created file
#     return latest_file

# file_names = ["first", "second", "third", "fourth", "fifth"]  # Add more names as needed
# current_index = 0

# while True:
#     input("Press Enter to continue or type 'quit' to exit: ")
    
#     if input().lower() == "quit":
#         break

#     source_file = get_latest_file('.')  # Get the latest file in the current directory
#     if source_file is None:
#         print("No files found in the directory.")
#         continue

#     if current_index < len(file_names):
#         copy_destination_file = file_names[current_index]
#         current_index += 1
#     else:
#         print("No more predefined filenames available.")
#         continue

#     source_file = ensure_py_extension(source_file)
#     copy_destination_file = ensure_py_extension(copy_destination_file)

#     print(f"Source File: {source_file}")
#     print(f"Destination File: {copy_destination_file}")

#     # Add your file copying logic here

import os
import glob
import shutil
import time

def ensure_py_extension(filename):
    if not filename.endswith('.py'):
        filename += '.py'
    return filename

def get_latest_file(directory):
    list_of_files = glob.glob(os.path.join(directory, '*'))  # Get all files in the directory
    if not list_of_files:
        return None
    latest_file = max(list_of_files, key=os.path.getctime)  # Get the latest created file
    return latest_file

file_names = ["first", "second", "third", "fourth", "fifth"]  # Add more names as needed
current_index = 0

while True:
    user_input = input("Press Enter to continue or type 'quit' to exit: ")
    if user_input.lower() == "quit":
        break

    source_file = get_latest_file('.')  # Get the latest file in the current directory
    if source_file is None:
        print("No files found in the directory.")
        continue

    if current_index < len(file_names):
        copy_destination_file = file_names[current_index]
        current_index += 1
    else:
        print("No more predefined filenames available.")
        continue

    source_file = ensure_py_extension(source_file)
    copy_destination_file = ensure_py_extension(copy_destination_file)

    source = f"/Users/shiveshrichhariya/Desktop/GITHUB/100 DAYS OF CODE/PYTHON.100DAYSCODE/Tkinter Learning/{source_file}"
    destination = f"/Users/shiveshrichhariya/Desktop/GITHUB/100 DAYS OF CODE/PYTHON.100DAYSCODE/Tkinter Learning/{copy_destination_file}"

    destination_dir = os.path.dirname(destination)
    if not os.path.exists(destination_dir):
        print(f"Creating directory: {destination_dir}")
        os.makedirs(destination_dir)

    if os.path.exists(source):
        print("Processingggggg!! ⏳")
        shutil.copy(source, destination)
        print("Done Shivesh Boss")
    else:
        print(f"Source file does not exist, please try again")
    
    time.sleep(1)
