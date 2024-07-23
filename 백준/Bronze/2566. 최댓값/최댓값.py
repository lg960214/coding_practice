N = 9

arr = []

for i in range(N):
    temp_lst = list(map(int, input().split()))
    arr.append(temp_lst)

mi = 0
mj = 0
max_ = -1e9

for i in range(N):
    for j in range(N):
        if (max_ < arr[i][j]):
            max_ = arr[i][j]
            mi = i
            mj = j

print(max_)
print(mi+1, mj+1)