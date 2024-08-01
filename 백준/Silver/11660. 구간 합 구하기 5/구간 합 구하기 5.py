import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
N, M = map(int, input().split())

c_arr = [[0]*(N+1)]

for i in range(N):
    temp_lst = list(map(int, input().split()))
    c_arr.append([0] + temp_lst)

# 2차원 누적합 적용
# arr[0][1] += arr[0][0]
# arr[0][2] += arr[0][0]
# ...
#
# arr[1][1] += arr[1][0]
# arr[1][2] += arr[1][1]
# ...
#
# arr[N-1][1] += arr[1][0]
# arr[N-1][2] += arr[1][1]
# ...

# 1. 가로합
for i in range(1, N+1):
    for j in range(2, N+1):
        c_arr[i][j] += c_arr[i][j-1]

# 2. 세로합
for i in range(1, N+1):
    for j in range(2, N+1):
        c_arr[j][i] += c_arr[j-1][i]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(c_arr[x2][y2] - c_arr[x1-1][y2] - c_arr[x2][y1-1] + c_arr[x1-1][y1-1])