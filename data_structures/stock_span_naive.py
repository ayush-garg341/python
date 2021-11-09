"""
    Calculate the days for which the stock has highest price.

    The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before 
    the given day, for which the price of the stock on the current day is less than its price on the given day. 

    input -> stock price per day list
    output -> stock spanning list

    eg. 
    input P = [100, 80, 60, 70, 60, 75, 85]
    output S = [1, 1, 1, 2, 1, 4, 6]
"""


def stock_spanning_list(stock_price_list):
    span = [1]*len(stock_price_list)
    for i in range(0, len(stock_price_list)):
        count = 1
        for j in range(i-1, -1, -1):
            if stock_price_list[j] < stock_price_list[i]:
                count += 1
            else:
                break

        span[i] = count

    return span


stock_price = [100, 80, 60, 70, 60, 75, 85]
print(stock_spanning_list(stock_price))
