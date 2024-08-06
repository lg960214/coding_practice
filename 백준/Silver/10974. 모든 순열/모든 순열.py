def rec(n, lst=[]):
    if (n >= N):
        print(*lst)
        return

    for i in range(1, N+1):
        if (i in lst): continue
        lst.append(i)
        rec(n+1, lst)
        lst.pop()


N = int(input())
rec(0)