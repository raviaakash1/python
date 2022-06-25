# Names , Variables , Code , Functions

# Functions Do three things:
#       1. They name peices of code the way variables name strings and numbers.
#       2. They take arguments the way your script takes argv
#       3. Using 1 and 2, they let you make your own "mini-script" or "tiny commands".

#  Create functions using dev keyword


def print_two(*args):
    arg1, arg2 = args
    print(f"arg1 : {arg1}  arg2 : {arg2}")

def print_two_again(arg1,arg2):
    print(f"arg1 : {arg1}  arg2 : {arg2}")

def print_one(arg1):
    print(f"arg1 : {arg1}")

def print_none():
        print("I got nothing")

print_two("Aakash","Ravi")
print_two_again("Ravi","Aakash")
print_one("Ravi")
print()