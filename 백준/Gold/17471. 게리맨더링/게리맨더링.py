# 구상
# DFS로 조합 만들고, UF 로 연결여부 확인 및 최솟값 갱신
# 인원 적으니 인접리스트 대신 인접행렬로

def Find(now):
    if now == parents[now]: return now
    parents[now] = Find(parents[now])
    return parents[now]

def Union(a, b):
    root_A = Find(a)
    root_B = Find(b)
    if root_A == root_B: return

    parents[max(root_A, root_B)] = min(root_A, root_B)

def simulate(team1, team2):
    global min_
    # parents 초기화
    for i in range(N):
        parents[i] = i

    # 구역 합치기
    for i in range(len(team1)):
        for j in range(i+1, len(team1)):
            if adj_matrix[team1[i]][team1[j]] == 1:
                Union(team1[i], team1[j])

    for i in range(len(team2)):
        for j in range(i+1, len(team2)):
            if adj_matrix[team2[i]][team2[j]] == 1:
                Union(team2[i], team2[j])

    # 그룹이 2개 이상이면 break
    group_cnt = 0
    for i in range(N):
        if Find(i) == i:
            group_cnt += 1

    if group_cnt != 2:
        return


    population_1 = 0
    population_2 = 0

    for p in team1:
        population_1 += people[p]

    for p in team2:
        population_2 += people[p]

    min_ = min(min_, abs(population_1 - population_2))




def rec(step, idx, thr):
    if step >= thr:
        mine = []
        opponent = []
        for i in range(N):
            if visit[i] == True:
                mine.append(i)
            else:
                opponent.append(i)
        simulate(mine, opponent)
        return

    for i in range(idx, N):
        visit[i] = True
        rec(step+1, i+1, thr)
        visit[i] = False


N = int(input())

parents = [i for i in range(N)]

people = list(map(int, input().split()))

adj_matrix = [[0]*N for _ in range(N)]
for i in range(N):
    tmp = list(map(lambda x: int(x)-1, input().split()))
    for el in tmp[1:]:
        adj_matrix[i][el] = 1
        adj_matrix[el][i] = 1

min_ = 1001
visit = [False]*N
for num in range(1, (N//2)+1):
    rec(0, 0, num)

if min_ == 1001:
    print(-1)
else:
    print(min_)
