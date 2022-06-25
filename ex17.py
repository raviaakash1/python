# More on files


# Copying one files data to another file

from sys import argv
from ex16 import get_abs_path
from os.path import exists

def copy_data_from_one_file_another(in_file,out_file):
    in_file_abs_path = get_abs_path(in_file)
    out_file_abs_path = get_abs_path(out_file)

    

    if exists(in_file_abs_path):

        in_file_data = str()
        
        with open(in_file_abs_path,"r") as readPtr:
            in_file_data = readPtr.read()

        with open(out_file_abs_path,"w") as writePtr:
            writePtr.write(in_file_data)

        print(f"data copied from {in_file} to {out_file}")

if __name__ == "__main__":
    script, in_file, out_file = argv

    # doiing it all in one line
    # open(out_file,"w").write(open(in_file,"r").read())

    copy_data_from_one_file_another(in_file,out_file)




