N, M = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

flag = True
cx = 0
cy = 0
di = 1

def move(d):
    global cx, cy, di, flag

    tx = cx + int(d)*dx[di]
    ty = cy + int(d)*dy[di]

    if tx < 0 or ty < 0 or tx > N or ty > N:
        flag = False
        return

    cx = tx
    cy = ty

    return

def turn(d):
    global di
    if d == '1':
        di = (di + 1)%4

    elif d == '0':
        di = (di + 3)%4

for _ in range(M):
    command, d = input().split()


    if command == 'MOVE':
        move(d)
    elif command == 'TURN':
        turn(d)


if flag:
    print(cx, cy)
else:
    print(-1)