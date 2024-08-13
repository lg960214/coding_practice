N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N # 원소는 무조건 자기가 1개인 수열을 갖는다

for i in range(N):
    target_num = arr[i]
    for j in range(i - 1, -1, -1):
        comp_num = arr[j]
        if (comp_num < target_num):
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))