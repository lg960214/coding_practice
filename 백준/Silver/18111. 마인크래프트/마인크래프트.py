land = []

N, M, B = map(int, input().split())
min_height = 1e9
max_height = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    land.append(temp)
    min_height = min(min(temp), min_height)
    max_height = max(max(temp), max_height)

def mine_time(land, height):
    time = 0
    for i in range(N):
        for j in range(M):
            if land[i][j] > height:
                time += (land[i][j] - height) * 2
            elif land[i][j] < height:
                time += height - land[i][j]
    return time

# 견적 짜는거 추가
blocks = 0
for s in range(N):
    blocks += sum(land[s])
blocks += B

min_time = blocks*2
min_height_result = 0

for h in range(max_height+1):
    if blocks < N*M*h:
        continue
    h_time = mine_time(land, h)
    if h_time <= min_time:
        min_time = h_time
        min_height_result = h

print(min_time, min_height_result)