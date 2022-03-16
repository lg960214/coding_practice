import sys
input = sys.stdin.readline

K, N = map(int, input().split())
li = []
for _ in range(K):
    li.append(int(input()))

ans = [1, (1 + max(li)) // 2, max(li)]
result = 0
while (ans[0] != ans[1] and ans[1] != ans[2]) or N > result:
    result = sum([i // ans[1] for i in li])
    if N > result:
        ans[2] = ans[1]
        ans[1] = (ans[0] + ans[1]) // 2
    else:
        ans[0] = ans[1]
        ans[1] = int((ans[1] + ans[2]) / 2 + 0.5)
    result = sum([i // ans[1] for i in li])

print(ans[1])