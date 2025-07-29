# check if given string is palindrome or not
def check_palindrome(string: str, start_index: int = 0) -> bool:
    if start_index == len(string)//2:
        return True
    return check_palindrome(string, start_index + 1) if string[start_index] == string[len(string) - 1 - start_index] else  False

if __name__ == "__main__":
    string: str = input("Enter a String >> ")
    is_palindrome: bool = check_palindrome(string)
    print(f"The given string is {'palindrome' if is_palindrome else 'not a palindrome'}")