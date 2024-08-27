

def go_spin(idx, l_lst, r_lst):
    global arr
    for i, el in enumerate(l_lst):
        if i == 0: continue
        if el == -1:
            tmp = arr[idx-i][0]
            arr[idx-i] = arr[idx-i][1:] + [tmp]
        else:
            tmp = arr[idx-i][-1]
            arr[idx-i] = [tmp] + arr[idx-i][:-1]

    for i, el in enumerate(r_lst):
        if el == -1:
            tmp = arr[idx+i][0]
            arr[idx+i] = arr[idx+i][1:] + [tmp]
        else:
            tmp = arr[idx+i][-1]
            arr[idx+i] = [tmp] + arr[idx+i][:-1]

def spin(n, d): # n 번 움직여라 / d : 1 -> 시계방향, d : -1 -> 반시계방햐
    # 오른쪽
    # idx=2와 idx=6을 비교
    right_spin = [d]
    left_spin = [d]

    prev = n-1
    di = d # 움직일 방향

    for i in range(n, 4):
        if arr[prev][2] == arr[i][6]: # 같으면
            break
        else:
            right_spin.append(-di)
            di = -di
            prev = i


    prev = n-1
    di = d
    # 왼쪽
    for i in range(n-2, -1, -1):
        if arr[prev][6] == arr[i][2]:
            break
        else:
            left_spin.append(-di)
            di = -di
            prev = i

    go_spin(n-1, left_spin, right_spin)

arr = [list(map(int, list(input()))) for _ in range(4)]
K = int(input())
for _ in range(K):
    n, d = map(int, input().split())
    spin(n, d)

print(arr[0][0] + 2*arr[1][0] + 4*arr[2][0] + 8*arr[3][0])


