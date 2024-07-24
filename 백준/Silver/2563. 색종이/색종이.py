
arr = [[0]*101 for i in range(101)]

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())

    for i in range(10):
        for j in range(10):
            arr[x+i][y+j] = 1

sum_ = 0
for i in range(101):
    for j in range(101):
        if (arr[i][j] == 1):
            sum_ += 1

print(sum_)