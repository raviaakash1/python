def get_fibonacci_number(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 1
    return get_fibonacci_number(num - 1) + get_fibonacci_number(num - 2)
    

if __name__ == "__main__":
    num: int = int(input("Enter a number > "))
    fib_num: int = get_fibonacci_number(num)
    print(f"fibonacci number for {num} is {fib_num}")