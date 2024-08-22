# @ 문제 분석

# [1] 문제 조건
#  - N이닝동안 게임 진행
#    - 3아웃 시 이닝 종료 <-> 공격 수비 전환

#  - 타순 정하기 ( 경기 중에 변경 불가 )
#    - 이닝이 변경되어도 순서 유지
#      - ex) 2이닝 6번 타자 마지막 --> 3이닝 7번 타자
#  - 9번 타자까지 공 쳤는데 3아웃 x --> 이닝은 안 끝나고 1번부터 선다
#
#  - 1 2 3 -> 홈 : 1점
#  - 루에 머물러있기 가능 (주자) / 이닝 시작 시 주자는 x
#  - 공 칠 때 결과
#    - 안타, 2루타, 3루타, 홈런, 아웃
#
#
# [2] 시간복잡도
#   - 완전 탐색 : 타자 배치 경우의 수 : 9! - 362,880
import sys

visit = [False]*9

def play(lst):
    lst = lst[:3] + [0] + lst[3:]
    base = [0, 0, 0, 0]
    taja_idx = 0
    score = 0
    for i in range(N):
        # 게임 시작
        o = 0
        base[3] = base[2] = base[1] = 0
        while True:

            taja_result = ining_result[i][lst[taja_idx]]
            if taja_result == 0: # 아웃
                o += 1
                if o == 3: # 3아웃
                    break

            elif taja_result == 1: # 1루타
                score += base[3]
                base[3] = base[2]
                base[2] = base[1]
                base[1] = 1

            elif taja_result == 2: # 2루타
                score += base[3] + base[2]
                base[3] = base[1]
                base[2] = 1
                base[1] = 0

            elif taja_result == 3: # 3루타
                score += base[3] + base[2] + base[1]
                base[3] = 1
                base[2] = 0
                base[1] = 0

            else: # 홈런
                score += base[3] + base[2] + base[1] + 1
                base[3] = 0
                base[2] = 0
                base[1] = 0

            if taja_idx < 8:
                taja_idx += 1
            else:
                taja_idx = 0

        if taja_idx < 8:
            taja_idx += 1
        else:
            taja_idx = 0

    return score

def rec(step, lst):
    global max_
    if (step >= 8):
        res = play(lst)
        max_ = max(max_, res)
        return

    for i in range(1, 9):
        if visit[i] == True: continue
        visit[i] = True
        rec(step+1, lst + [i])
        visit[i] = False


N = int(input())

ining_result = [list(map(int, input().split())) for _ in range(N)]

max_ = 0
rec(0, [])

print(max_)