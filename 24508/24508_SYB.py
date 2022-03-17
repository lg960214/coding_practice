import sys
input = sys.stdin.readline

N, K, T = map(int, input().split())
basket = list(map(int, input().split()))
li = [0 for _ in range(K)]
sorted_basket = []
for i in basket:
    li[i] += 1
for i in range(K):
    for j in range(li[i]):
        sorted_basket.append(i)

cnt = 0
l, r = 0, N - 1
while l < r:
    if sorted_basket[r] >= K:
        sorted_basket[r - 1] += (sorted_basket[r] - K)
        sorted_basket[r] = 0
        r -= 1
    else:
        sorted_basket[r] += sorted_basket[l]
        cnt += sorted_basket[l]
        sorted_basket[l] = 0
        l += 1

sorted_basket[l] = sorted_basket[l] % K

if cnt <= T and sorted_basket[l] == 0:
    print("YES")
else:
    print("NO")
