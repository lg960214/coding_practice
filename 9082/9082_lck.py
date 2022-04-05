import sys

sys.stdin = open("testcase.txt", "r")
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    data = [
        list(input().strip()) if x == 1 else list(map(int, list(input().strip())))
        for x in range(2)
    ]
    answer = 0

    for i in range(n):
        if i >= 1 and i < n - 1:
            if (
                not data[0][i - 1] == 0
                and not data[0][i] == 0
                and not data[0][i + 1] == 0
            ):
                answer += 1
                data[0][i - 1] -= 1
                data[0][i] -= 1
                data[0][i + 1] -= 1
        elif i == 0:
            if not data[0][i] == 0 and not data[0][i + 1] == 0:
                answer += 1
                data[0][i] -= 1
                data[0][i + 1] -= 1
        elif i == n - 1:
            if not data[0][i - 1] == 0 and not data[0][i] == 0:
                answer += 1
                data[0][i] -= 1
                data[0][i - 1] -= 1

    print(answer)
