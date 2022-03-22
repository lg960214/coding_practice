import itertools

N, K = map(int, input().split())
get_weight = list(map(int, input().split()))
count = 0

for orders in itertools.permutations([i for i in range(N)], N):
    WEIGHT=500
    for order in orders:
        WEIGHT -= K
        WEIGHT += get_weight[order]
        if WEIGHT < 500:
            break
    else:
        count += 1
print(count)
