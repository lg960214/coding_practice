import sys
input = sys.stdin.readline

n = int(input().strip())
assignments = [list(map(int, input().split())) for _ in range(n)]
assignments.sort(key=lambda x: x[1])
result = assignments[-1][1]
for i in range(len(assignments) - 1, -1, -1):
    d, t = assignments[i]
    result = min(result, t) - d

print(result)
