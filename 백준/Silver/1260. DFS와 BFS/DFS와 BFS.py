N, M, V = map(int, input().split())

adj_lst = [[] for _ in range(N+1)]

visit = [False]*(N+1)

for _ in range(M):
    v1, v2 = map(int, input().split())
    adj_lst[v1].append(v2)
    adj_lst[v2].append(v1)

for l in adj_lst:
    l.sort()

def dfs(cur_v):
    print(cur_v, end=' ')
    global visit

    visit[cur_v] = True
    stk = []

    while True:
        for next_v in adj_lst[cur_v]:
            if (visit[next_v] == True): continue
            visit[next_v] = True
            # error : next_v가 아닌 cur_v 추가해야 함
            stk.append(cur_v)
            cur_v = next_v
            print(cur_v, end=' ')
            break
        else:
            if stk:
                cur_v = stk.pop()
            else:
                break

def bfs(cur_v):
    global visit

    visit[cur_v] = False

    q = [cur_v]

    while q:
        cur_v = q.pop(0)
        print(cur_v, end=' ')
        for next_v in adj_lst[cur_v]:
            if (visit[next_v] == False): continue
            visit[next_v] = False
            q.append(next_v)

dfs(V)
print()
bfs(V)