T = int(input())

for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = True
    # 가로
    for i in range(9):
        set_ = set()
        for j in range(9):
            set_.add(arr[i][j])
        if (len(set_) != 9):
            flag = False

    # 세로
    for i in range(9):
        set_ = set()
        for j in range(9):
            set_.add(arr[j][i])
        if (len(set_) != 9):
            flag = False

    # Square
    for x in range(3):
        for y in range(3):
            set_ = set()
            for i in range(x*3, (x+1)*3):
                for j in range(y*3, (y+1)*3):
                    set_.add(arr[i][j])
            if (len(set_) != 9):
                flag = False

    if (flag):
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
