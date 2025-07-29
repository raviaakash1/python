def factorial(num : int) -> int:
    return  1 if num == 0 or num == 1  else num*factorial(num-1)

if __name__ == "__main__":
    num : int = int(input("Enter a number > "))
    print(f"factorial of the number {num} -> ",factorial(num))