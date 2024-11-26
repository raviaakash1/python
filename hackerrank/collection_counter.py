from collections import Counter
def calc_earnings(shoe_size, price, list_counter):
    if shoe_size in list_counter.keys():
        if list_counter[shoe_size] != 0:
            list_counter[shoe_size] -= 1
            return price
    return 0

if __name__ == "__main__":
    total_earning = 0
    num_of_shoes = int(input())
    list_of_shoes_avaiable = [int(data) for data in input().split(' ')]
    list_counter = Counter(list_of_shoes_avaiable)
    num_of_customers = int(input())
    for i in range(num_of_customers):
        data = input().split(' ')
        shoe_size = int(data[0])
        price = int(data[1])
        total_earning += calc_earnings(shoe_size, price, list_counter)
        

    print(total_earning)