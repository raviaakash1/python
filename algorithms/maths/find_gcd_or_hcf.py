def gcd(num1, num2):
    lower_number = num1 if num1 < num2  else num2
    for i in range(lower_number, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i

# 2nd solution would be to use Euclidean Algorithm
def gcd_using_euclidean_algo(a, b):
    while (a != b):
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# optimized Euclidean Algo
def opt_eucd_algo(a,b):
    if b == 0:
        return a
    return opt_eucd_algo(b , a%b)
if __name__ == "__main__":
    num1, num2 = input("Please Enter a number : ").split(" ")
    # print(gcd(int(num1), int(num2)))
    print(gcd_using_euclidean_algo(int(num1), int(num2)))
    print(opt_eucd_algo(int(num1), int(num2)))