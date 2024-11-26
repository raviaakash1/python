def lcm(a, b):
    max = a if a > b else b

    for i in range(max , a*b +  1, 1):
        if i % a == 0 and i % b == 0:
            print(i)
            return

#  efficient solution
#  a*b = gcd(a,b) * lcm(a,b)

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def eff_lcm(num1, num2):
    print((num1*num2)/gcd(num1, num2))

if __name__ == "__main__":
    num1 , num2 = input("Please Enter a number : ").split(" ")
    num1 = int(num1)
    num2 = int(num2)
    lcm(num1, num2)
    # efficent_way
    eff_lcm(num1, num2)