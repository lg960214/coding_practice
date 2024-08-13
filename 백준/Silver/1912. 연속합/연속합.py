# @ 문제 분석
# 1. 문제 조건
# - "연속한 수를 선택"
# - "최대의 합"
# - "N은 최대 100,000"
#
# 위의 조건으로 말미암아 봤을 때, O(N)으로 해결해야 된단 사실을 깨달았고,
# dp table을 활용하기 위한 조건들을 생각해봤다.

# @ dp[n+1]과 dp[n]의 관계
# - dp[n]의 내용은 "n까지 연속한 수의 최대 합"이 될 것이다.
# - dp[n+1]은 dp[n]으로부터 구해지며, dp[n]과 arr[n+1]이 더해졌을 때와
#   연관지으면 될 것이다.
#   - dp[n] < 0 이라면, arr[n+1]이 dp[n+1]이 될 것이고
#   - dp[n] >= 0 이라면, arr[n+1] + dp[n]이 dp[n+1]이 될 것이다.

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N

dp[0] = arr[0]

for i in range(1, N):
    if dp[i - 1] >= 0:
        dp[i] = dp[i - 1] + arr[i]
    else:
        dp[i] = arr[i]

print(max(dp))
