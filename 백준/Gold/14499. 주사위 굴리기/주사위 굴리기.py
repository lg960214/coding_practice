# @ 검증


dice = dict()
dice['u'] = 0
dice['d'] = 0
dice['f'] = 0
dice['b'] = 0
dice['l'] = 0
dice['r'] = 0


def roll(d):
    tmp = dice['u']
    if d == 1: # 동
        dice['u'] = dice['l']
        dice['l'] = dice['d']
        dice['d'] = dice['r']
        dice['r'] = tmp

    elif d == 2: # 서
        dice['u'] = dice['r']
        dice['r'] = dice['d']
        dice['d'] = dice['l']
        dice['l'] = tmp

    elif d == 3: # 북
        dice['u'] = dice['f']
        dice['f'] = dice['d']
        dice['d'] = dice['b']
        dice['b'] = tmp

    elif d == 4: # 남
        dice['u'] = dice['b']
        dice['b'] = dice['d']
        dice['d'] = dice['f']
        dice['f'] = tmp

    return

N, M, sx, sy, K = map(int, input().split())

dx = [0, 0, 0, -1, 1] # 동 서 북 남
dy = [0, 1, -1, 0, 0]

x = sx
y = sy

arr = [list(map(int, input().split())) for _ in range(N)]

howTo = list(map(int, input().split()))


for d in howTo:
    nx = x + dx[d]
    ny = y + dy[d]
    # 정육면체는 격자판 밖으로 이동할 수 없습니다.
    # 만약 바깥으로 이동시키려고 하는 시도가 있을 때, 해당 시도를 무시하며 출력도 하지 않습니다.
    if 0 > nx or 0 > ny or N <= nx or M <= ny: continue
    x = nx
    y = ny
    # 주사위 굴린다
    roll(d)

    if arr[x][y] == 0:
        arr[x][y] = dice['d']
    elif arr[x][y] != 0:
        dice['d'] = arr[x][y]
        arr[x][y] = 0

    print(dice['u'])