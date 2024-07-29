arr = [list(map(int, input().split())) for _ in range(5)]
visit = [[0]*5 for _ in range(5)]

call = []

for i in range(5):
    tmp = list(map(int, input().split()))
    call += tmp

ans = 0

for i in range(len(call)):
    # 1. 값 체크
    target = call[i]
    for a in range(5):
        for b in range(5):
            if (arr[a][b] == target):
                visit[a][b] = 1

    # 2. 빙고인 지 체크
    cnt = 0

    # 2-1. 가로
    for a in range(5):
        if (sum(visit[a]) == 5):
            cnt += 1

    # 2-2. 세로
    for a in range(5):
        sum_ = 0
        for b in range(5):
            sum_ += visit[b][a]
        if (sum_ == 5):
            cnt += 1

    # 2-3. 대각1
    sum_ = 0
    for a in range(5):
        sum_ += visit[a][a]
    if (sum_ == 5):
        cnt += 1

    # 2-4. 대각2
    sum_ = 0
    for a in range(5):
        sum_ += visit[4-a][a]
    if (sum_ == 5):
        cnt += 1

    if (cnt >= 3):
        ans = i+1
        break

print(ans)