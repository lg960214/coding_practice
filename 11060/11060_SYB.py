import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
cnt = [li[0]] + [0 for _ in range(N-1)]

for i in range(N):
    t = [0 for _ in range(N)]

    for idx in range(N):
        if cnt[idx] != 0:
            for j in range(li[idx]):
                try:
                    t[j+idx+1] = 1
                except Exception:
                    pass
    if t[-1] == 1:
        print(i+1)
        cnt = t
        break
    cnt = t

if N == 1:
    print(0)
elif cnt[-1] == 0:
    print(-1)