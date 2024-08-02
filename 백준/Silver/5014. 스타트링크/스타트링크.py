# 틀린 원인 : Edge Case - 시작이 도착점

# 1층부터 시작, 가장 높은 층 : F
# 강호가 있는 층 : S
# 스타트링크가 있는 층 : G
# 위로 이동 가능 : U 칸 만큼
# 아래로 이동 가능 : D 칸 만큼
from collections import deque

def bfs(start):
    if (S == G): return 0
    
    q = deque()
    visit = set()

    visit.add(start)
    q.append(start)

    step = 0
    curSize = 0

    while q:
        curSize = q.__len__()

        for c in range(curSize):
            target = q.popleft()

            # 강호가 탄 엘리베이터는 버튼이 2개
            for i in range(2):
                if (i == 0):
                    # 1. Up
                    next = target + U
                    # 제한 조건 : U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다
                    # 1층부터 시작하고, F층까지 존재
                    if not (1 <= next <= F): continue
                    if (next == G): return step+1
                    if (next in visit): continue
                    visit.add(next)
                    q.append(next)


                if (i == 1):
                    # 2. Down
                    next = target - D
                    if not (1 <= next <= F): continue
                    if (next == G): return step+1
                    if (next in visit): continue
                    visit.add(next)
                    q.append(next)
        step += 1

    # 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력
    return -1

F, S, G, U, D = map(int, input().split())

ans = bfs(S)

if (ans == -1):
    print('use the stairs')
else:
    print(ans)