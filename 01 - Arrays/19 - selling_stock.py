from sys import stdin


def getMaximumProfit(values, n) :
    # We shall find local minima and local maxima throughout the stocks
    # as we are allowed to do multiple transactions, we shall buy at
    # local minima and sell at local maxima and then move to next.

    profit = 0
    i = 0

    # traves only till b4 n-1 as we are accessing i+1 
    while i < n-1:

        # find local minima
        while i < n-1 and values[i+1] <= values[i]:
            i += 1

        # If we reached end then break
        if i == n-1:
            break 

        buy = i

        i+=1
        # find local maxima
        while i < n-1 and values[i+1] >= values[i]:
            i += 1
        
        sell = i 

        # print(buy, sell)
        profit += (values[sell] - values[buy])

    return profit

        





#taking input using fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    values = list(map(int, stdin.readline().rstrip().split(" ")))
    return values, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    values, n = takeInput()
    print(getMaximumProfit(values, n))
    t -= 1
