N, M = map(int, input().split())

target_list = list(range(1, N+1))

for _ in range(M):
    A, B = map(int, input().split())
    temp_list = target_list[A-1:B][::-1]

    for i in range(0, B-A+1):
        target_list[i+A-1] = temp_list[i]

for i in range(len(target_list)):
    print(target_list[i], end=' ')

