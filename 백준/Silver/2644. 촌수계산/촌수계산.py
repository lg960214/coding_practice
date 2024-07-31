from collections import deque

def bfs(S, G):

    q = deque()
    visit = [False]*(n+1)

    q.append(S)
    visit[S] = True

    step = 0
    curSize = 0

    while q:
        curSize = len(q)
        for c in range(curSize):
            target = q.popleft()

            for next_v in adj_lst[target]:
                if (next_v == G): return step+1
                if (visit[next_v] == True): continue
                visit[next_v] = True
                q.append(next_v)
        step+= 1
    return -1


n = int(input())
S, G = map(int, input().split())
m = int(input())


adj_lst = [[] for _ in range(n+1)]


for _ in range(m):
    v1, v2 = map(int, input().split())
    adj_lst[v1].append(v2)
    adj_lst[v2].append(v1)

    ans = bfs(S, G)

print(ans)
