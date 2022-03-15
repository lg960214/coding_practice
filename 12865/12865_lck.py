import sys

input = sys.stdin.readline

n, k = map(int, input().split())

wv_list = []
for _ in range(n):
    wv_list.append(list(map(int, input().split())))


dp = [0 for _ in range(k + 1)]

indices = [k]
for i in range(n):
    temp_dp = dp[:]
    for j in set(indices):
        next_weight = j - wv_list[i][0]
        if next_weight >= 0:
            dp[next_weight] = max(dp[next_weight], temp_dp[j] + wv_list[i][1])
            indices.append(next_weight)

print(max(dp))
