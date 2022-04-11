import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    stocks = list(map(int, input().split()))
    profit, price_sell, num_stocks, cost = 0, 0, 0, 0

    for n in reversed(range(N)):
        if stocks[n] >= price_sell:
            profit += price_sell * num_stocks - cost
            price_sell, num_stocks, cost = stocks[n], 0, 0
        else:
            num_stocks += 1
            cost += stocks[n]
    if num_stocks:
        profit += price_sell * num_stocks - cost
    print(profit)