N, K = map(int, input().split())

arr = []

for i in range(N):
    num, g, s, c = map(int, input().split())
    temp_lst = [g,s,c,num]
    arr.append(temp_lst)

arr.sort(reverse=True)

ranking = [i for i in range(1, N+1)]


for i in range(N-1):
    prev = arr[i][:3]
    for j in range(1, N):
        next = arr[j][:3]

        if (prev == next):
            ranking[j] = ranking[i]
        else:
            break

for i in range(N):
    if (arr[i][3] == K):
        print(ranking[i])
        break