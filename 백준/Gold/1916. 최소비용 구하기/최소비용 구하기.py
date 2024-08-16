import os, io
import heapq as hq

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

INF = int(1e8) # 초기값 : node 최대 개수 x edge 값 최대 범위

N = int(input())
M = int(input())

adj_lst = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2, w = map(int, input().split())
    adj_lst[v1].append((w, v2))

S, E = map(int, input().split())

heap = list()
hq.heappush(heap, (0, S))

dist = [INF]*(N+1)
dist[S] = 0

while heap:
    cur_d, cur_v = hq.heappop(heap)

    if (dist[cur_v] < cur_d): continue # 지금까지의 경로가 기록된 최소 경로보다 길면 버린다
    if cur_v == E: # 도착점까지의 최단 경로는 바로 얻어진다
        break
    for next_w, next_v in adj_lst[cur_v]:
        next_cost = dist[cur_v] + next_w

        if dist[next_v] > next_cost:
            dist[next_v] = next_cost
            hq.heappush(heap, (next_cost, next_v))

print(dist[E])
