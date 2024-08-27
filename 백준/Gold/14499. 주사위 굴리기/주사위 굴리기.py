def oob(r, c):
    return 0 > r or r >= N or 0 > c or c >= M


def change_dice(s1, s2, s3, s4, s):
    if not s % 2:
        dice_dict[s1], dice_dict[s2], dice_dict[s3], dice_dict[s4] = \
            dice_dict[s4], dice_dict[s3], dice_dict[s1], dice_dict[s2]
    else:
        dice_dict[s4], dice_dict[s3], dice_dict[s1], dice_dict[s2] = \
            dice_dict[s1], dice_dict[s2], dice_dict[s3], dice_dict[s4]


def spin_dice(s):
    if s < 2:  # 동서
        change_dice('d', 'u', 'l', 'r', s)
    else:  # 북남
        change_dice('d', 'u', 'b', 'f', s)


def simulate():
    r, c = x, y

    for spin in move:
        # 굴릴 좌표의 바닥 위치
        row, col = r + DIR[spin][0], c + DIR[spin][1]
        if oob(row, col): continue
        spin_dice(spin)
        if not MAP[row][col]:
            # 지도가 0일 경우
            MAP[row][col] = dice_dict['d']
        else:
            # 지도가 0이 아닐 경우
            dice_dict['d'] = MAP[row][col]
            MAP[row][col] = 0
        print(dice_dict['u'])

        r, c = row, col


N, M, x, y, k = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

dice_dict = {noodle: 0 for noodle in 'udfblr'}

move = list(map(lambda x: int(x) - 1, input().split()))

DIR = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 동서북남

simulate()
