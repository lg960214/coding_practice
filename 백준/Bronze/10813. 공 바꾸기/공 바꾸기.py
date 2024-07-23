N, M = map(int, input().split())

list_ = [i for i in range(0, N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    list_[a], list_[b] = list_[b], list_[a]

for i in range(1, N + 1):
    print(list_[i], end=' ')