import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    li = list(map(int, input().split()))

    max_num, cnt = 0, 0
    for i in range(N-1, -1, -1):
        if li[i] < max_num:
            cnt += (max_num - li[i])
        else:
            max_num = li[i]
    print(cnt)