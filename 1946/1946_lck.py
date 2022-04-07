import sys

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    data = [list(map(int, input().strip().split())) for _ in range(n)]
    data.sort(key=lambda x: x[0])

    maximum = data[0][1]
    answer = 1

    for i in range(1, n):
        if data[i][1] < maximum:
            maximum = data[i][1]
            answer += 1

    print(answer)
