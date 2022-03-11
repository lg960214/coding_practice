def solve(li):
    end = False
    for i in range(5, 24):
        for j in range(1, 20):
            if li[i][j] + li[i+1][j] + li[i+2][j] + li[i+3][j] + li[i+4][j] == 5:
                if li[i-1][j] == 0 and li[i + 5][j] == 0:
                    end = True
            if li[i][j] + li[i][j+1] + li[i][j+2] + li[i][j+3] + li[i][j+4] == 5:
                if li[i][j - 1] == 0 and li[i][j + 5] == 0:
                    end = True
            if li[i][j] + li[i+1][j+1] + li[i+2][j+2] + li[i+3][j+3] + li[i+4][j+4] == 5:
                if li[i - 1][j - 1] == 0 and li[i + 5][j + 5] == 0:
                    end = True
            if li[i][j] + li[i-1][j+1] + li[i-2][j+2] + li[i-3][j+3] + li[i-4][j+4] == 5:
                if li[i + 1][j - 1] == 0 and li[i - 5][j + 5] == 0:
                    end = True
    return end


N = int(input())

white = [[0 for _ in range(25)] for __ in range(29)]
black = [[0 for _ in range(25)] for __ in range(29)]

answer = -1
for c in range(N):
    y, x = map(int, input().split())

    if answer == -1:
        if c % 2 == 0:
            black[y + 4][x] = 1
            if solve(black):
                answer = c + 1
        else:
            white[y + 4][x] = 1
            if solve(white):
                answer = c + 1

print(answer)