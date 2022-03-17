import sys

input = sys.stdin.readline

n, k, t = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

if not sum(data) % k == 0:  # 터지지 않고 남는 것이 있을 때
    print("NO")
else:
    quotient = sum(data) // k
    remainder_sum = sum(data[quotient:])
    if remainder_sum > t:
        print("NO")
    else:
        print("YES")
