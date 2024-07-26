land = []

N, M, B = map(int, input().split())
min_height = 0
max_height = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    max_height += sum(temp)
    land.append(temp)

max_height += B
max_height //= N*M

def mine_time(land, height, inven):
    time = 0
    for i in range(N):
        for j in range(M):
            if land[i][j] > height:
                time += (land[i][j] - height) * 2
            elif land[i][j] < height:
                time += height - land[i][j]
    return time
min_time = 1e9
for i in range(min_height, max_height+1):
    i_time = mine_time(land, i, B)
    if i_time <= min_time:
        min_time = i_time
        min_height_result = i

print(min_time, min_height_result)