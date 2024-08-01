# Cycle 조건 : 새로 들어온 node의 root가 같은 node를 가진다.

def Find(now):
    if (now == parent[now]):
        return now
    parent[now] = Find(parent[now])
    return parent[now]

def Union(a, b):
    root_A = Find(a)
    root_B = Find(b)

    if (root_A == root_B): return

    if (root_A < root_B):
        parent[root_B] = root_A
    else:
        parent[root_A] = root_B

    return

N, M = map(int, input().split())

parent = [i for i in range(N+1)]

flag = False
ans = 0
for i in range(M):
    a, b = map(int, input().split())

    if flag: continue
    
    # 이미 부모가 같다 = 싸이클 완성
    if (Find(a) == Find(b)):
        flag = True
        ans = i+1
    else:
        # 부모가 다르면 병합
        Union(a, b)

print(ans)