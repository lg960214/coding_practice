"""
오류 원인 : 최솟값
threshold 완벽하게 계산해본다고 2*N으로 했다가 틀림
속편하게 N^2으로 크게 잡자

오류 원인2 : 비활성 --> 활성
아몰랑~ 하고 문제분석 때 넘어갔던 조건을 다시 보니 걸렸다
"--> 읽어보니 차이 없네 그냥 on/off 인듯" <-- 안 적어놓았으면 못 찾았을 듯

@ 문제 분석
 [1] 문제 조건
   - 바이러스 : 활성 or 비활성
   - 처음엔 비활성 상태
   - 활성 상태인 애들은 인접 빈칸으로 동시 복제 (1초)
   - 바이러스 M개를 활성 상태로 변경하려고 한다

   - 연구소 : 빈 칸(0), 벽(1), 바이러스(2)
   - 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변함
     --> 활성 바이러스가 그냥 퍼지는 거랑 무슨 차이지?
     --> 읽어보니 차이 없네 그냥 on/off 인듯

 [2] 시간복잡도 (간단 설계 버전)
   연구소 크기 (N=50), 바이러스 최대 10개

   1. dfs로 조합 구함 = 10C5 = 252
   2. 시뮬레이션 진행
     - BFS 진행 (최대 100초) = 2500 + a

   시간 초과는 나지 않을 듯 하다

 [3] 이외 조건
   - 연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다.
   - 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.
     --> 해당 조건에 유의할 것


@ 검증
활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변함
  --> 써 놓은 이유가 있었다


"""
from collections import deque

def BFS(virus_lst):
    q = deque()
    visit = [[0]*N for _ in range(N)]

    for loc in virus_lst:
        q.append(loc)

    for loc in virus_loc:
        if loc in virus_lst:
            visit[loc[0]][loc[1]] = 1
        else:
            visit[loc[0]][loc[1]] = -1 # 비활성 표시

    visit_cnt = 0
    step = 0
    curSize = 0
    while q:
        if all_empty_cnt == visit_cnt:
            return True, step

        curSize = q.__len__()

        for c in range(curSize):
            target = q.popleft()

            for i in range(4):
                nx = target[0] + dx[i]
                ny = target[1] + dy[i]
                if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
                if arr[nx][ny] == 1: continue
                if visit[nx][ny] == -1: # 비활성
                    visit[nx][ny] = 1
                    q.append((nx, ny)) # 활성으로
                if visit[nx][ny] > 0: continue
                visit_cnt += 1
                visit[nx][ny] = 1
                q.append((nx, ny))

        step += 1

    return False, -1

def make_combi(step, idx, lst):
    global min_
    if step >= M:
        flag, t = BFS(lst)
        if flag:
            min_ = min(min_, t)
        return

    for i in range(idx, virus_cnt):
        make_combi(step+1, i+1, lst + [virus_loc[i]])


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

min_ = 2501
virus_loc = []

all_empty_cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus_loc.append((i, j))

        if arr[i][j] == 0:
            all_empty_cnt += 1

virus_cnt = len(virus_loc)
make_combi(0, 0, [])

if min_ == 2501:
    print(-1)
else:
    print(min_)