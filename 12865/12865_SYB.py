import sys
input = sys.stdin.readline

N, K = map(int, input().split())
li = []
answer = [[0 for _ in range(K+1)] for __ in range(N+1)]
for i in range(N):
    li.append(list(map(int, input().split())))

for i in range(N):
    w, v = li[i]
    for j in range(K+1):
        answer[i+1][j] = answer[i][j]

    for j in range(K-w+1):
        if answer[i][w + j] < (answer[i][j] + v):
            answer[i + 1][w + j] = (answer[i][j] + v)
        else:
            answer[i + 1][w + j] = answer[i][w + j]

print(max(answer[-1]))