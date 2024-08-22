# 16722. 결합 / 풀이 시간 : 48분
#
# @ 문제 분석 (3분 30초)
#
# [1] 문제 조건 1 : 세 가지 속성
#  - 모양 : {동그라미, 세모, 네모}
#  - 도형의 색 : {노란색, 빨간색, 파란색}
#  - 배경색 : {회색, 흰색, 검은색}
#
#  - 세 가지 속성이 모두 같거나, 모두 다른 세 장의 그림 조합을 찾기
#
# [2] 문제 조건 2 : 점수
#  - 0점으로 시작
#  - 행동 1 (합) : 그림 세장이 "합" 이라면 +1, 아니라면 -1
#  - 행동 2 (결) : "합" 이 없다면 +3, 아니라면 -1
#
# [3] 입/출력 분석
#  - 도형 모양, 도형 색, 배경색
#
# [4] 시간복잡도
#  - 결을 한 번 구해놓고 시작해야 한다
#  - 조합 경우의 수 : 9C3 = 84
#  - 미리 계산하고 결 계산을 진행한다면, 시간초과 날 일은 없다
#
#
#
# @ 설계 (2분 30초)
# [1] 함수
#  - "결" 판단 함수 : 현재 조합이 있는 지 검사
#    - 외치지 않은 "합"이 없다
#    - "결"을 통해 3점을 얻은 적이 없어야 한다.
#
#  - "합" 판단 함수 :
#    - 이전에 외친 적이 없어야 한다
#    - "합"이 되어야 한다
#
# @ 검증
# 1. 문제 조건 다시 점검 -> 완료
# 2. 논리대로 흘러갔는 지, 머리에 한 번에 보일 정도로 체크 --> 완료

final_set = set()
cur_set = set()

S_dict = {'CIRCLE' : 0, 'TRIANGLE' : 1, "SQUARE" : 2}
C_dict = {'YELLOW' : 0, 'RED' : 1, 'BLUE' : 2}
B_dict = {'GRAY' : 0, 'WHITE' : 1, 'BLACK' : 2}

S_arr = [[]]
C_arr = [[]]
B_arr = [[]]

for i in range(9):
    target = input().split()
    S_arr.append(S_dict[target[0]])
    C_arr.append(C_dict[target[1]])
    B_arr.append(B_dict[target[2]])

N = int(input())

combine_flag = False
score = 0

def check_case(step, idx, lst):
    if step >= 3:
        bine(lst[0], lst[1], lst[2], 1)
        return

    for i in range(idx, 10):
        lst.append(i)
        check_case(step+1, i+1, lst)
        lst.pop()

def com(): # 모든 가능한 조합 검사
    # 2-1. 합과 다르면, False
    # 2-2. 합과 같으면, True
    if len(final_set - cur_set) == 0:
        return True
    return False

def bine(x1, x2, x3, flag):
    # 1. 모양이 모두 같거나, 모두 다른 지 체크
    S_set = set([S_arr[x1], S_arr[x2], S_arr[x3]])
    if len(S_set) == 2:
        return False
    # 2. 색깔이 모두 같거나, 모두 다른 지 체크
    C_set = set([C_arr[x1], C_arr[x2], C_arr[x3]])
    if len(C_set) == 2:
        return False
    # 3. 배경이 모두 같거나, 모두 다른 지 체크
    B_set = set([B_arr[x1], B_arr[x2], B_arr[x3]])
    if len(B_set) == 2:
        return False

    # 모두 뚫었다면, True 반환
    tmp_lst = [x1, x2, x3]
    tmp_lst.sort()
    if flag == 1: # final_set 만드는 중이라면
        final_set.add(tuple(tmp_lst))
    else:
        if tuple(tmp_lst) in cur_set: # 마지막 : 기존에 외친 것이라면, False 반환
            return False
        cur_set.add(tuple(tmp_lst))
    return True

check_case(0, 1, [])

for i in range(N):
    tmp = input().split()

    if tmp[0] == 'G': # 결!
        if combine_flag == True: # "결"을 통해 3점을 얻은 적이 있다면
            score -= 1
        else:
            if com():
                score += 3
                combine_flag = True
            else:
                score -= 1

    elif tmp[0] == 'H': # 합!
        if bine(int(tmp[1]), int(tmp[2]), int(tmp[3]), 0):
            score += 1
        else:
            score -= 1

print(score)