N, M = map(int, input().split())

arr = []

for i in range(N):
    temp_lst = list(map(str, input()))
    arr.append(temp_lst)

ans = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    for j in range(M):
        if (arr[i][j] == 'c'):
            ans[i][j] = 0
            continue

        flag = True
        cnt = 1
        for k in range(j-1, -1, -1):
            if (arr[i][k] == 'c'):
                break
            cnt += 1
        else:
            flag = False

        if (flag):
            ans[i][j] = cnt
        else:
            ans[i][j] = -1




for i in range(N):
    for j in range(M):
        print(ans[i][j], end=' ')
    print()

