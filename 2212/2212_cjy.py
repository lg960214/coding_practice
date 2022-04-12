import sys
input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())
loc = sorted(map(int, input().split()))
dist = sorted([loc[i + 1] - loc[i] for i in range(len(loc) - 1) if loc[i + 1] - loc[i]])
if K >= N:
    print(0)
elif K == 1:
    print(sum(dist))
else:
    print(sum(dist[:-(K - 1)]))
