n, k, t = map(int, input().split())
buckets = sorted(map(int, input().split()))
right = n - 1
left = 0

while t and left < right:
    buckets[right] = buckets[right] % k
    buckets[left] = buckets[left] % k
    while not buckets[right] and left < right:
        right -= 1
    while not buckets[left] and left < right:
        left += 1
    else:
        if buckets[left] <= t:
            if buckets[right] + buckets[left] < k:
                num_move = buckets[left]
            else:
                num_move = k - buckets[right]
            t -= num_move
        else:
            num_move = t
            t = 0
        buckets[right] += num_move
        buckets[left] -= num_move
buckets[right] = buckets[right] % k
buckets[left] = buckets[left] % k
if sum(buckets):
    print('NO')
else:
    print('YES')