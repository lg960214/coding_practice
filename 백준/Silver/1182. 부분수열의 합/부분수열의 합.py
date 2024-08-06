N, S = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0

# 2진법 활용
# i가 2진법 수의 자리수를 순회하며 1인 경우에만 더하도록 구성
# ex) 01100 -> i가 2, 3일 때의 부분집합의 합을 구함
for bm in range(1, 1<<N):
    sum_ = 0
    for i in range(N):
        if bm & (1<<i):
            sum_ += arr[i]
    if (sum_ == S):
        answer += 1

print(answer)