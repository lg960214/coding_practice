N, K, T = map(int, input().split())
basket = list(map(int, input().split()))
basket.sort()

cnt = 0
l, r = 0, N - 1
while l < r:
    if basket[r] >= K:
        basket[r - 1] += (basket[r] - K)
        basket[r] = 0
        r -= 1
    else:
        basket[r] += basket[l]
        cnt += basket[l]
        basket[l] = 0
        l += 1

basket[l] = basket[l] % K

if cnt <= T and basket[l] == 0:
    print("YES")
else:
    print("NO")