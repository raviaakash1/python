from typing import List

def get_input() -> List :
    user_input : List= input("Enter a list of numbers to be sorted : ").split(" ")
    
    if len(user_input) < 1 or user_input == ['']:
        return user_input
    else:
        user_input = [float(i) if i.find(".") != -1 else int(i) for i in user_input]
    return user_input

if __name__ == "__main__":
    user_input: List = get_input()
    