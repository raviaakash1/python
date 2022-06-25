# Functions and Files

from ex16 import get_abs_path
from sys import argv

def print_all_content(file):
    print(f"data in file {file.name} :\n{file.read()}")
    # import pdb; pdb.set_trace()
    # print(dir(file))
    # print("File experiment :; ",file.fileno())

def rewind(file):
    file.seek(0)

def print_a_line(line_count,file):
    print(line_count,file.readline(),end = " ")

if __name__ == "__main__":
    script, fileName = argv
    file_abs_path = get_abs_path(fileName)

    with open(file_abs_path, "r") as readPtr:
        # read all data of the file
        print_all_content(readPtr)
        #  rewinind the file
        rewind(readPtr)

        line_number = 1

        print_a_line(line_number, readPtr)
        print_a_line(line_number+1, readPtr)
        print_a_line(line_number + 2, readPtr)