N, M = map(int, input().split())

arr = []

for i in range(N):
    temp_list = list(map(str, input()))
    arr.append(temp_list)

max_ = 1

fin = False

for s in range(min(N, M), 1, -1):
    if (fin):
        break
    for i in range(0, N-s+1):
        if (fin):
            break
        for j in range(0, M-s+1):
            if (fin):
                break
            if (arr[i][j] == arr[i+s-1][j] == arr[i][j+s-1] == arr[i+s-1][j+s-1]):
                max_ = s
                fin = True
                break



print(max_**2)