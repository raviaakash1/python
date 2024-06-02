# find max elem make has table of that size iterate the list and increase the index by 1 check if after increment its equal to 2 print index
# pythonic way create a dict with elem as key and value as 0 increment val if found if value is 2 print key
# use 2 for loops to find the elem
# can sort the array then check



def find_first_duplicate(arr):
    hash_table = [0]*len(arr)
    for index, elem in enumerate(arr):

# driver code
if __name__ == "__main__":
    arr = [10, 5, 3, 4, 3, 5, 6]
    find_first_duplicate(arr)
