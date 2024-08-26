#
# 시간복잡도
# 사람이 100명, 병원이 13개
# 병원 13개 중 7개 뽑는 경우의 수 = 13C7 = 1,716
# 총 계산 시간복잡도 = 171,600 + a
# 터지지는 않는다

def cal_dist(lst):
    global min_

    dist = 0

    for i, j in human:
        local_min_dist = 1e9
        for x, y in lst:
            tmp_dist = abs(i-x) + abs(j-y)
            local_min_dist = min(tmp_dist, local_min_dist)
        dist += local_min_dist

    min_ = min(dist, min_)

def combination(step, idx, lst=[]):
    if step >= M:
        cal_dist(lst)
        return

    for i in range(idx, len(hospital)):
        combination(step+1, i+1, lst+[hospital[i]])


N, M = map(int, input().split())
min_ = 1e9

arr = [list(map(int, input().split())) for _ in range(N)]

human = []
hospital = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            human.append((i, j))
        elif arr[i][j] == 2:
            hospital.append((i, j))


combination(0, 0)

print(min_)