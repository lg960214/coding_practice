# @ 문제 분석
#
# [1] 문제 조건
# - 길이가 N / 위도 N 아래도 N
#   - 시간복잡도를 고려했을 때, array 2개로 짜도 된다
#   - robot array 2개, 내구도 array 2개
#
# - 종료 조건
#   - 4번 단계에서 종료 가능
#   - step을 세야 한다
#
# [2] 시간복잡도
#  1. Ai 번 이동 = 100*4 = 4000
#  2. 로봇 탐색 = 100
#  3. pass
#  4. 내구도 탐색 = 100*2
#  5. 최대 반복 : 2000
#  --> 5000 x 1000 = 10,000,000
#  --> 시간복잡도에 걸릴 일은 없다
#
# @ 검증
# --> "가장 먼저 올라간 로봇부터" 조건 빠트려서, 다시 구현
# --> down arr에 해당하는 로봇은 필요없으므로, 제거
# --> 로봇 옮겼으면, 자리를 비워주는 것 구현


N, K = map(int, input().split())

tmp_lst = list(map(int, input().split()))

up_arr = tmp_lst[:N]
down_arr = tmp_lst[N:][::-1]

up_robot = [False]*N

step = 1 # 1단계부터 시작

while True:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    tmp_up = up_arr[-1]
    tmp_up_r = up_robot[-1]
    for i in range(N-1, 0, -1):
        up_arr[i] = up_arr[i-1]
        up_robot[i] = up_robot[i-1]

    up_robot[0] = False    # 검증 때 구현
    up_arr[0] = down_arr[0]

    # -- up_arr 정리 완료
    for i in range(N-1):
        down_arr[i] = down_arr[i+1]
    down_arr[N-1] = tmp_up
    # -- down_arr 정리 완료

    # 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
    if up_robot[-1] == True:
        up_robot[-1] = False

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로
    for i in range(N-2, -1, -1):
        if up_robot[i] == True:
            # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며,
            if up_robot[i+1] == True: continue
            # 그 칸의 내구도가 1 이상 남아 있어야 한다.
            if up_arr[i+1] == 0: continue
            # 한 칸 이동할 수 있다면 이동한다.
            up_arr[i+1] -= 1
            up_robot[i+1] = True
            up_robot[i] = False
            # 만약 이동할 수 없다면 가만히 있는다.

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면
    # 올리는 위치에 로봇을 올린다.
    if up_arr[0] != 0:
        # 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면
        # 그 칸의 내구도는 즉시 1만큼 감소한다.
        up_arr[0] -= 1
        up_robot[0] = True

    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
    # 그렇지 않다면 1번으로 돌아간다.
    k_cnt = 0
    for i in range(N):
        if up_arr[i] == 0:
            k_cnt += 1
        if down_arr[i] == 0:
            k_cnt += 1

    if k_cnt >= K:
        break

    step += 1

print(step)