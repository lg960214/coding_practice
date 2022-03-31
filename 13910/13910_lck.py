import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int,input().strip().split())
data = list(map(int,input().split()))
data.append(0)
data = list(combinations(data,2))
data = [sum(x) for x in data]
data = set(data)

check_list = []
new_check = []
dp = [10000] * (n+1)

for wok in data:
    if wok <= n:
        dp[wok] = 1
        check_list.append(wok)

while True:
    count = 0
    for check in check_list:
        for wok in data:
            if check + wok <= n and dp[check + wok] > dp[check] + 1:
                dp[check+wok] = dp[check] + 1
                new_check.append(check+wok)
                count += 1
    if count == 0:
        break
    check_list = new_check[:]
    new_check = []
    

if dp[-1] == 10000:
    print("-1")
else:
    print(dp[-1])
