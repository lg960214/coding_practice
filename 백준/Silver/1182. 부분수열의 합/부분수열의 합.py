N, S = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0

for bm in range(1, 1<<N):
    sum_ = 0
    for i in range(N):
        if bm & (1<<i):
            sum_ += arr[i]
    if (sum_ == S):
        answer += 1

print(answer)