# there are multiple logics which can be used here


# initially we can divide the problem for odd and even numbers

def check_digits(number):
    res = 0
    while number > 0:
        number = number // 10
        res+=1
    return res

def check_palindrome(integer):
    # count digits
    total_digits = check_digits(integer)
    integer = str(integer)
    
    if total_digits % 2 == 1:
        # odd use case
        mid_index = total_digits // 2
        start_index = 0
        end_index = total_digits - 1
        for i in range(mid_index):
            if integer[start_index] != integer[end_index] :
                print(f"{integer} is not a palindrome")
                return
            start_index += 1
            end_index -= 1
    else:
        # even use case
        start_index = 0 
        end_index = total_digits - 1
        while start_index - end_index <= 1:
            if integer[start_index] != integer[end_index]:
                print(f"{integer} is not a palindrome")
                return
            start_index += 1
            end_index -= 1
    print(f"{integer} is a palindrome")


# 2nd method
# reverse a given number
def reverse(integer):
    res = 0
    # count = 10**(check_digits(integer)-1)
    
    # print(count)
    while integer > 0:
        rem = integer % 10
        integer = integer // 10
        res = res*10 + (rem)
        # count /= 10
    print(res)
    return int(res) 
def check_palindrome_2(integer):
    if reverse(integer) == integer:
        print(f"{integer} is a palindrome")
        return
    print(f"{integer} is not a palindrome")
if __name__ == "__main__":
    # check_palindrome(int(input("Please Enter a number : ")))
    check_palindrome_2(int(input("Please Enter a number : ")))
