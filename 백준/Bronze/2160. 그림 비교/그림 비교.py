N = int(input())

arr_lst = []
for i in range(N):
    temp_list = [list(map(str, input())) for _ in range(5)]
    arr_lst.append(temp_list)

idx_1 = -1
idx_2 = -1
min_ = 1e9

for i in range(N-1):
    for j in range(i+1, N):
        arr_1 = arr_lst[i]
        arr_2 = arr_lst[j]

        cnt = 0

        for a in range(5):
            for b in range(7):
                if (arr_1[a][b] != arr_2[a][b]):
                    cnt += 1

        if (min_ > cnt):
            min_ = cnt
            idx_1 = i+1
            idx_2 = j+1

print(idx_1, idx_2)
