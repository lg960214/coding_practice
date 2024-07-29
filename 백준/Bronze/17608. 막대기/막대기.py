N = int(input())

stk = []

for i in range(N):
    tmp = int(input())

    for j in range(len(stk)):
        if (stk[-1] <= tmp):
            stk.pop()
        else:
            break
    stk.append(tmp)

print(len(stk))