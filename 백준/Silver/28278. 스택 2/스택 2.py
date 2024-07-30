import sys

input = sys.stdin.readline

N = int(input())
stk = []
for _ in range(N):
    temp = input().rstrip()
    if len(temp) == 1:
        rule = int(temp)
    else:
        rule, x = map(int, temp.split())
    if rule == 1:
        stk.append(x)
        continue
    elif rule == 2:
        if stk:
            print(stk.pop())
            continue
        else:
            print(-1)
            continue
    elif rule == 3:
        print(len(stk))
        continue
    elif rule == 4:
        if not stk:
            print(1)
            continue
        else:
            print(0)
            continue
    else:
        if stk:
            print(stk[-1])
            continue
        else:
            print(-1)
            continue