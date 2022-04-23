import sys
sys.stdin = open('testcase.txt', 'r')
input = sys.stdin.readline

n, k = map(int,input().strip().split())
data = list(map(int,input().strip().split()))

left = 0
right = sum(data) // k

while left <= right:
    center = (left + right) // 2
    num_sum = 0
    current_k = 0
    for num in data:
        num_sum += num
        if num_sum >= center:
            current_k += 1
            num_sum = 0

    if current_k >= k:
        left = center + 1
    elif current_k < k:
        right = center - 1

print((left + right) // 2)