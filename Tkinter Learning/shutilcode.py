import os
import shutil

def ensure_py_extension(filename):
    if not filename.endswith('.py'):
        filename += '.py'
    return filename

source_file=input("ENTER SOURCE FILE - ")
copy_desination_file=input("ENTER DESTINATION FILE - ")

source_file=ensure_py_extension(source_file)
copy_desination_file=ensure_py_extension(copy_desination_file)

source = f"/Users/shiveshrichhariya/Desktop/GITHUB/100 DAYS OF CODE/Tkinter Learning/{source_file}"
destination = f"/Users/shiveshrichhariya/Desktop/GITHUB/100 DAYS OF CODE/Tkinter Learning/{copy_desination_file}"
 
destination_dir = os.path.dirname(destination)
if not os.path.exists(destination_dir):
        os.makedirs(destination_dir) 

# if os.path.exists(source):
shutil.copy(source , destination)