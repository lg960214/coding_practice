# 오류 원인 : 문제 조건 놓침
# arr 크기는 100이 아니라 101이다

# @ 문제 분석
# dragon curve를 그리는 것이 관건으로 보임
# 좌표를 기준으로 90도 선형 변환을 하는 문제
# 공식을 유추해보니, 90도 선형 변환하면 된다
# ( 0 -1 ) ( a )  =  (-b )
# ( 1  0 ) ( b )  =  ( a )

# @ 설계
# 1. 드래곤 커브를 그린다
#  - 20개
# 2. 정사각형을 찾는다
#  - 크기가 1인 것부터 100까지
#   --> 시간 초과 안남

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def make_dragon_curve(step):
    if step >= g:
        return

    # 현재 끝 점 저장
    trans_x = dragon_loc[-1][0]
    trans_y = dragon_loc[-1][1]

    for i in range(len(dragon_loc)-2, -1, -1): # 끝 점이 맨 뒤에 와야 해서, 앞에서부터 시작
        # 1. 좌표 변환
        cur_x = dragon_loc[i][0] - trans_x
        cur_y = dragon_loc[i][1] - trans_y
        # 2. 선형 변환
        cur_x, cur_y = cur_y, -cur_x
        cur_x += trans_x
        cur_y += trans_y
        # 3. 좌표 저장
        dragon_loc.append((cur_x, cur_y))

    make_dragon_curve(step+1)


arr = [[False]*101 for _ in range(101)]

N = int(input())
# 1. Dragon Curve 좌표 찍기
for _ in range(N):
    y, x, d, g = map(int, input().split())

    dragon_loc = [(x, y), (x+dx[d], y+dy[d])]
    make_dragon_curve(0)

    for i, j in dragon_loc:
        # 입력으로 주어지는 드래곤 커브는 격자 밖으로 벗어나지 않는다.
        # 드래곤 커브는 서로 겹칠 수 있다.
        arr[i][j] = True

# 2. 정사각형 찾기
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            cnt += 1
print(cnt)
