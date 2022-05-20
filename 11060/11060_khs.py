n = int(input())
m = list(map(int, input().split()))

num = n+1
dp = [num] * n

dp[0] = 0

for i in range(n):
    for j in range(1,m[i]+1):
        ind = i+j
        if ind >= n:
            break
        dp[ind] = min(dp[ind], dp[i]+1)

answer = dp[-1]
if answer == n+1:
    print(-1)
else:
    print(answer)