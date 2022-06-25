# Reading and Writing Files


"""
Some common commands which are used on the regular basis
    close               --> Closes the file, after saving it.
    read                --> Reads the whole content of the file.
    reeadline           --> Read just one line of the file
    truncate            --> Expties the file.
    write('stuff')      --> use to write string to the file
    seek(0)             --> this statement will move the read/write pointer to the beginning of the file
    seek(n)             --> this will move the read/write pointer to the nth file

    Why use seek?
        for example lets say we have a CD player with 10 songs, with the help of seek we can change the songs and jump from one track to another
        if we dont have seek then we will have to read it line by line (byte by byte)

"""

from sys import argv
from os import path

def get_abs_path(file_name,file_type = 'in'):
    folder_abs_path = path.join(path.dirname(__file__),"in_files" if file_type == "in" else "out_files")
    file_abs_path = path.join(folder_abs_path,file_name)
    return file_abs_path

def read_file(file_name):

    file_abs_path = get_abs_path(file_name,file_type = "in")
    print(file_abs_path)

    with open(file_abs_path,"r") as readPtr:
        file_data = readPtr.read()
        return file_data

def write_file(file_name):
    file_abs_path = get_abs_path(file_name,file_type = "out")

    with open(file_abs_path,"w") as writePtr:
        user_data = input("Enter data ==> ")
        writePtr.write(user_data)

        print("-"*5,"Data Written Successfully","-"*5)
    return None

def create_file(file_name):
    write_file(file_name)

if __name__ == "__main__":
    # script, filename = argv
    prompt = " >"
    while True:
        print("Commands :: ",end = ' ')
        print("""
            1. Read File
            2. Write File
            3. Create File
        """)

        user_input = int(input(prompt))
        file_name = input(f"Enter filename {prompt}")
        
        returned_data = read_file(file_name) if user_input == 1 else None
        write_file(file_name) if user_input == 2 else None
        create_file(file_name) if user_input ==3 else None

        print(returned_data) if user_input ==1 else None

