import sys

input = sys.stdin.readline

t = int(input())
data = []
for _ in range(t):
    input()
    data.append(list(map(int, input().split())))

for price in data:
    day = 0
    profit = 0
    local_maximum = max(price[day:])
    length = len(price)
    last_profit_day = 0
    if local_maximum == price[0]:
        pass
    else:
        while day < length - 1:
            if price[day + 1] == local_maximum:
                profit += local_maximum * (day - last_profit_day + 1) - sum(
                    price[last_profit_day : day + 1]
                )
                if day < length - 2:
                    local_maximum = max(price[day + 2 :])
                last_profit_day = day + 2
            day += 1

    print(profit)
