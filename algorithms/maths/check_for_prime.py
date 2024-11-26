import math
def check_for_prime(num):
    flag = False
    if num == 1:
        print("Not a prime number")
        return
    for i in range(2, num+1):
        if num % i == 0:
            if flag:
                print("Not a prime number")
                return
            flag = True
    print("Prime Number")


# effecient solution
def eff_check_prime(num):
    # check till sqrt of num
    if num == 1:
        print("Not a prime number")
        return
    i = 2 * 2
    # while i <= num:  #this can also be used
    #     if num % i == 0:
    #         print("Not a prime number")
    #         return
    #     i = i*i
    # print("It is a prime number")

    for i in range(2,math.ceil(math.sqrt(num))):
        if num % i == 0:
            # import pdb;pdb.set_trace()
            print("Not a prime NUmber")
            return
    print("Its a prime number")

# def more_eff_check_prime(num):
#     if num == 1:
#         print("Not a prime")
#         return
#     if num == 2 or num == 3:
#         print("Prime")
#         return
#     if num % 2 == 0  or num %3 == 0:
#         print("Not Prime")
#         return
    
#     for i in range(5, )

if __name__ == "__main__":
    num1 = input("Please Enter a number : ")
    num = int(num1)
    check_for_prime(num)
    eff_check_prime(num)
    # more_eff_check_prime(num)