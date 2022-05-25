n,N = list(map(int, input().split()))
s = list(map(int, input().split()))
if N == 1:
    if n % s[0] == 0:
        print(n//s[0])
    else:
        print(-1)
else:
    from itertools import combinations
    sum_s = [sum(i) for i in list(combinations([0]+s,2))]
    sum_s = sorted(sum_s)
    dp = [n//min(s)+min(s)] * (n+1)
    dp[0] = 0
    for i in range(n+1):
        for j in sum_s:
            if i + j > n:
                break
            dp[i+j] = min(dp[i+j],dp[i] + 1)

    if dp[-1] == n//min(s)+min(s):
        print(-1)
    else:
        print(dp[-1])