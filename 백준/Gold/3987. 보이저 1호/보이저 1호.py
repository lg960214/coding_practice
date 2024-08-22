# @ 문제 분석 (~58)
# 주어진 방향으로 쭉 이동하는데, 탐사할 때 행성에 의해 방향이 변하는 문제
#
# [1] 문제 조건
#  A. 종료 : 블랙홀을 만나기 or 외부 좌표로 벗어나기
#  - 인접한 칸으로 이동하는 데 걸리는 시간은 1초
#
#  B. 반사 방향
#  a. d == 0
#    - / : 1
#    - \ : 3
#  b. d == 1
#    - / : 0
#    - \ : 2
#  c. d == 2
#    - / : 3
#    - \ : 1
#  d. d == 3
#    - / : 2
#    - \ : 0
# --> 위의 경우로 보면, '/' : [1, 0, 3, 2]
#                      '\' : [3, 2, 1, 0]
#
#  C. 순환하는 경우
#   - 같은 방향으로 또 돌아온다면, 순환이다
#   - 4xNxM visit에 방향을 저장하면 될 것 같다
#
#

# @ 설계
#  [1] 이동 : step에 + 1을 더함
#    - '.' 을 만나면 직진 이동
#    - '/\' 을 만나면 이동 후 조건부 방향 전환
#    - OOB 또는 블랙홀은 이동 후 종료
#
#  [2] 최댓값 갱신
#    - 최댓값이 갱신될 때마다 array를 비운다
#    - U R D L 순서이므로, 그냥 index 오름차순 후 출력하면 된다
#
#  [3] 순환 조건
#    - visit이 True이면 종료 후 Voyager 출력
#
#
# @ 구현 (~36)

def move(s_x, s_y, d):
    global loop_flag

    x = s_x - 1
    y = s_y - 1
    di = d

    visit = [[[False]*4 for _ in range(M)] for __ in range(N)]

    step = 0
    while True:
        nx = x + dx[di]
        ny = y + dy[di]
        if nx < 0 or ny < 0 or nx >= N or ny >= M: # 벗어나면 종료
            return step + 1
        if arr[nx][ny] == 'C': # 종료조건 : 블랙홀도 종료
            return step + 1

        if arr[nx][ny] == '/': # 종료조건 : 행성계 방향 체크
            if visit[nx][ny][di] == True:
                loop_flag = True
                return -1
            visit[nx][ny][di] = True
            x = nx
            y = ny
            di = reflect_dict['/'][di]
            step += 1
        elif arr[nx][ny] == '\\': # 행성계 방향 체크
            if visit[nx][ny][di] == True:
                loop_flag = True
                return -1
            visit[nx][ny][di] = True
            x = nx
            y = ny
            di = reflect_dict['\\'][di]
            step += 1

        if arr[nx][ny] == '.': # 빈 공간은 방문 체크만 하고 통과
            if visit[nx][ny][di] == True:
                loop_flag = True
                return 1e9
            visit[nx][ny][di] = True
            x = nx
            y = ny
            step += 1


reflect_dict = {'/': [1, 0, 3, 2], "\\": [3, 2, 1, 0]}
numToStr = ['U', 'R', 'D', 'L']

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_ = 0
max_direction_lst = []
loop_flag = False

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

sx, sy = map(int, input().split())

for i in range(4):
    res = move(sx, sy, i)
    if loop_flag: # 순환 상태인 지
        max_direction_lst = [i]
        break
    if res > max_:
        max_ = res
        max_direction_lst = [i]
    elif res == max_:
        max_direction_lst.append(i)

if loop_flag:
    print(numToStr[max_direction_lst[0]])
    print('Voyager')
else:
    max_direction_lst.sort()
    print(numToStr[max_direction_lst[0]])
    print(max_)
