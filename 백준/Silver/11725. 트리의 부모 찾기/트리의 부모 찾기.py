from collections import deque

def bfs(cur_v):
    global parents

    q = deque()

    q.append(cur_v)
    parents[cur_v] = cur_v

    while q:
        cur_v = q.popleft()

        for next_v in adj_lst[cur_v]:
            if (parents[next_v] != 0): continue
            parents[next_v] = cur_v
            q.append(next_v)

    return


N = int(input())

adj_lst = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)]

for _ in range(N-1):
    v1, v2 = map(int, input().split())

    adj_lst[v1].append(v2)
    adj_lst[v2].append(v1)

bfs(1)

for i in range(2, N+1):
    print(parents[i])

