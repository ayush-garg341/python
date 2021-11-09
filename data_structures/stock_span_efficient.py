from stack import Stack

def stock_spanning_list(stock_price_list):

    D = Stack()

    s = [1]*len(stock_price_list)
    for i in range(0, len(stock_price_list)):
        h = 0
        while not D.is_empty():
            if stock_price_list[i] > stock_price_list[D.top()]:
                D.pop()
            else:
                break
        if not D.is_empty():
            h = D.top() + 1
        s[i] = (i+1) - h
        D.push(i)
    
    return s


stock_price = [100, 80, 60, 70, 60, 75, 85, 105]
print(stock_spanning_list(stock_price))