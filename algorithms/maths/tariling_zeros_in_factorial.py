def find_factorial(num):
    if num == 0:
        return 1
    return num * find_factorial(num - 1)


def find_trailing_zeros(num):
    factorial = find_factorial(num)
    res = 0
    while factorial > 0:
        rem = factorial % 10
        if rem == 0:
            res += 1
        else:
            return res
        factorial = factorial // 10

# 2nd aproach (more efficient)
def find_trailing_zeros_eff(num):
    res = 0 
    i = 5
    while i <= num:
        res = res + num // i
        i *= 5
    return res
    

if __name__ == "__main__":
    print(find_trailing_zeros(int(input("Please enter a number : "))))
    print(find_trailing_zeros_eff(int(input("Please enter a number : "))))