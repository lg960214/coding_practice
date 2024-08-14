import os, io, sys

sys.setrecursionlimit(100000)
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def Union(node_a, node_b):
    pa = Find(node_a)
    pb = Find(node_b)

    if (pa == pb): return

    if (pa < pb):
        parent[pb] = pa
    else:
        parent[pa] = pb

def Find(now):
    if (now == parent[now]): return now

    parent[now] = Find(parent[now])
    return parent[now]


N, M = map(int, input().split())

parent = [i for i in range(N+1)]

for _ in range(M):
    flag, a, b = map(int, input().split())

    if not flag:
        Union(a, b)
    else:
        if Find(a) == Find(b):
            print('YES')
        else:
            print('NO')