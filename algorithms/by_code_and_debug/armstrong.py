'''
153  = 1^3 + 5^3 + 3^3 == 153 its armstrong
given a number num and number of digits in n then
    digit^n + ... == num then armstrong

'''
def get_num_digits(data : int) -> int:
    res : int = int(0)
    while data:
        res+=1
        data = data//10
    return res


def armstrong(data: int) -> bool:
    res: int = int(0)
    new_data = data
    num_digits: int = get_num_digits(data)
    while new_data:
        res = res+((new_data%10)**num_digits)
        new_data = new_data//10
    return res==data

def pythonic_way(data: int) -> bool:
    return sum(int(d) ** len(str(data)) for d in str(data)) == data

if __name__ == "__main__":
    data: int = int(input("Enter a digit >> "))
    print(armstrong(data))
    print(pythonic_way(data))