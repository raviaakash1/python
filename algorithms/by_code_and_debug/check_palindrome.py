def fast_approach(data: str) -> bool:
    return data == data[::-1]

def check_palindrome(data: str) -> bool:
    length = len(data)
    if length % 2 == 0:
        # here since step is -1 the start index becomes the end of the string and stop index is the middle of the string
        half_rev = data[:length//2 - 1:-1]
        return half_rev == data[:length//2]
    else:
        half_rev = data[:length//2:-1]
        return half_rev == data[:length//2]

if __name__ == "__main__":
    data: str = (input("Enter a digit >> "))
    is_pad: bool = fast_approach(data)
    is_palindrome: bool = check_palindrome(data)
    print(is_palindrome)
    print(is_pad)