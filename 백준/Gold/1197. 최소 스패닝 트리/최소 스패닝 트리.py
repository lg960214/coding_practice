import heapq as hq

def Find(now):
    if (now == parent[now]): return now

    parent[now] = Find(parent[now])
    return parent[now]

def Union(a, b):
    pa = Find(a)
    pb = Find(b)

    if (pa == pb): return

    if (pa < pb):
        parent[pb] = pa
    else:
        parent[pa] = pb

def kruskal():
    sm_w = 0

    while heap:
        w, v1, v2 = hq.heappop(heap)

        if (Find(v1) == Find(v2)): continue
        sm_w += w
        Union(v1, v2)

    return sm_w



N, M = map(int, input().split())

parent = [i for i in range(N+1)]

heap = []
for _ in range(M):
    v1, v2, w = map(int, input().split())

    hq.heappush(heap, (w, v1, v2))

ans = kruskal()

print(ans)