'''

given list of stock u need to determine when to buy and sell the stock

Restriction:
you cannot sell the stock on the same day when u bought it

prices = [7 2 1 5 6 4 8]

best time to buy would be when then stock price is 1 and to sell it would be when stock price is 8

if there is no profit to be gained then return 0

example : [8 5 3 2 1]
output = 0

'''

from typing import List


'''
def get_max_profit(prices: List[int]) -> int:
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        profit_today = prices[i] - min_price
        max_profit = max(max_profit, profit_today)
        min_price = min(min_price, prices[i])

    return max_profit


def get_max_profit(stock_price: List[int]) -> int:
    minimum: int = stock_price[0]
    maximum: int = stock_price[1]
    profit: int = 0
    index: int = 0
    
    while index < len(stock_price) - 1:
        if minimum -maximum > 0:
            if len(stock_price) - index == 2:
                return profit
            minimum = stock_price[index + 1]
            maximum = stock_price[index + 2]
        else:
            if minimum > stock_price[index]:
                minimum = stock_price[index]
            if maximum < stock_price[index + 1]:
                maximum = stock_price[index + 1]
            if maximum - minimum > profit:
                profit = maximum - minimum
        index += 1
    
    return profit
'''
import math
def get_max_profit(stock_price: List[int]) -> int:
    min_price = math.inf
    max_profit = 0
    for i in stock_price:
        min_price = min(min_price, i)
        max_profit = max(max_profit, i-min_price)
    return max_profit

if __name__ == "__main__":
    stock_price: List[int] = [int(i) for i in input("Enter stock price list >> ").split(" ")]
    max_profit: int = get_max_profit(stock_price)
    print(max_profit)