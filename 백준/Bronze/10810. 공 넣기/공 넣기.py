N, M = map(int, input().split())

list_ = [0]*(N+1)

for i in range(M):
    a, b, c = map(int, input().split())
    
    for k in range(a-1, b):
        list_[k] = c

for i in range(N):
    print(list_[i])




