# A. 퀵 정렬

def divide(x, y, size_):
    global blue, white

    if (size_ != 1):
        target_color = arr[x][y]
        flag = True

        for i in range(x, x + size_):
            if (flag == False):
                break
            for j in range(y, y + size_):
                if (arr[i][j] != target_color):
                    flag = False
                    break

        if (flag):
            if (target_color == 1):
                blue += 1
            else:
                white += 1
            return
        else:
            next_size = size_//2
            # 좌상
            divide(x, y, next_size)
            # 우상
            divide(x + next_size, y, next_size)
            # 좌하
            divide(x, y + next_size, next_size)
            # 우하
            divide(x + next_size, y + next_size, next_size)
    else:
        if (arr[x][y] == 1):
            blue += 1
        else:
            white += 1
        return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0

divide(0, 0, N)

print(white)
print(blue)