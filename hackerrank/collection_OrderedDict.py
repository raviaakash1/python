from collections import OrderedDict

if __name__ == "__main__":
    num_of_items = int(input())
    item_price_info = OrderedDict()

    for i in range(num_of_items):
        data = [data for data in input().split(' ') if data.strip() != '']
        if " ".join(data[:-1]) in item_price_info.keys():
            item_price_info[" ".join(data[:-1])] += int(data[-1])
        else:
            item_price_info[" ".join(data[:-1])] = int(data[-1])
    print("-------------------------------- Output --------------------------------")
    for item in item_price_info:
        print(item, " ", item_price_info[item])