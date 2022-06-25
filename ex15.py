# Reading files


# Importing necesssay modules for reading the file
from sys import argv
from os import path # using Os to get the path dynamically

# creating a function to read file
def read_file(file_abs_path):
    # creating a file object named f which stores files data and other info
    with open(file_abs_path,"r") as f:
        # print(dir(f))  --> uncomment this part to know what are the data members present for object f of type file
        data = f.read()
        return data
        

# Variable declaration
script, filename = argv

# getting path of the script and joining it with the input directory
folder_abs_path = path.join(path.dirname(__file__),"in_files")
# Now we have got the folder path, we just need to add the file name which we want to read 
file_abs_path = path.join(folder_abs_path,filename)

# reading files data and prinitng it
print(read_file(file_abs_path))

prompt = "Input another file name > "

# repeated as above
another_file_name = input(prompt)

file_abs_path = path.join(folder_abs_path,another_file_name)

print(read_file(file_abs_path))
