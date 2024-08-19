def rec(step):
    global flag
    if flag:
        return

    if step >= 15:
        for i in range(6):
            for j in range(3):
                if arr[i][j] != canBe[i][j]:
                    return
        flag = True
        return

    for i in range(3):
        team = case_lst[step][0]
        enemy = case_lst[step][1]
        if i == 0: # 앞이 이김
            if canBe[team][0] >= arr[team][0] or canBe[enemy][2] >= arr[enemy][2]: continue
            canBe[team][0] += 1
            canBe[enemy][2] += 1
            rec(step + 1)
            canBe[team][0] -= 1
            canBe[enemy][2] -= 1
        elif i == 1: # 무승부
            if canBe[team][1] >= arr[team][1] or canBe[enemy][1] >= arr[enemy][1]: continue
            canBe[team][1] += 1
            canBe[enemy][1] += 1
            rec(step + 1)
            canBe[team][1] -= 1
            canBe[enemy][1] -= 1

        else: # 뒤가 이김
            if canBe[team][2] >= arr[team][2] or canBe[enemy][0] >= arr[enemy][0]: continue
            canBe[team][2] += 1
            canBe[enemy][0] += 1
            rec(step + 1)
            canBe[team][2] -= 1
            canBe[enemy][0] -= 1


for _ in range(4):
    tmp_lst = list(map(int, input().split()))
    arr = []
    for i in range(0, len(tmp_lst), 3):
        arr.append(tmp_lst[i:i+3])
    canBe = [[0]*3 for _ in range(6)]

    case_lst = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
                (1, 2), (1, 3), (1, 4), (1, 5),
                (2, 3), (2, 4), (2, 5),
                (3, 4), (3, 5),
                (4, 5)]

    flag = False
    rec(0)

    if flag:
        print(1, end= ' ')
    else:
        print(0, end= ' ')