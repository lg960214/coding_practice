"""
@ 문제 분석

[1] 문제 조건
  - NxN 격자, 파이어볼 M개
  - 파이어볼 정보 : i, j, m, d, s (x좌표, y좌표, 질량, 방향, 속력)
  - 1번부터 N번까지 행과 열 번호가 매겨져 있다 + 1번은 N번과 연결

[2] 시간복잡도 : arr size - 50x50 (1 ~ N) / M - 50x50 / K = 1000
  1. 파이어볼 이동 : 2,500
    - q 활용

  2. 각 arr마다 합쳐짐 : 10,000
    - visit 활용 (3차원)
    - 조건에 따라 합치면 됨

  3. 반복횟수 : 1,000
    - 연산 횟수는 20,000,000이고 제한시간 1초이므로, 조심해서 짜야한다

[3] 공간복잡도 : stack 메모리 128MB로 가정
  - 최대 fireball 수 : 10,000
  - 들어가는 int : 5
  - int size = 28
    --> 50,000 x 150 = 7 500 000 B = 7MB / 일단 터지진 않는다

 @ 검증
  - 40:00 - q에 넣을 시, 좌표 제대로 기입안한 것 찾음

"""
from collections import deque

class Fire:
    def __init__(self, x, y, m, s, d):
        self.x = x
        self.y = y
        self.m = m
        self.s = s
        self.d = d

    def __repr__(self):
        return f'({self.x} {self.y} {self.m} {self.d} {self.s})'

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())

q = deque()
for _ in range(M):
    tx, ty, tm, ts, td = map(int, input().split())
    q.append(Fire(tx-1, ty-1, tm, ts, td))

for _ in range(K):
    # 1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    visit = [[[] for _ in range(N)] for _ in range(N)]

    for _ in range(q.__len__()):
        target = q.popleft()

        nx = (target.x + dx[target.d] * target.s) % N
        ny = (target.y + dy[target.d] * target.s) % N
        target.x, target.y = nx, ny

        visit[nx][ny].append(target)

    # 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다
    # 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.

    for i in range(N):
        for j in range(N):
            v_len = len(visit[i][j])
            if v_len == 0: continue

            if v_len == 1:
                q.append(visit[i][j][0])
                continue

            sm, ss = 0, 0
            oe_lst = [0, 0]
            for ball in visit[i][j]:
                sm += ball.m
                ss += ball.s
                oe_lst[ball.d%2] += 1

            sm //= 5
            ss //= len(visit[i][j])

            if sm == 0: continue

            if oe_lst.count(0): # 모두 홀수 or 모두 짝수
                for nd in [0, 2, 4, 6]:
                    q.append(Fire(i, j, sm, ss, nd))
            else:
                for nd in [1, 3, 5, 7]:
                    q.append(Fire(i, j, sm, ss, nd))

# 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.
total_mass = 0

while q:
    target = q.popleft()
    total_mass += target.m

print(total_mass)