import sys
from itertools import permutations
input = sys.stdin.readline

N, K = map(int, input().split())
li = list(map(int, input().split()))

li.sort(reverse=True)

list = list(permutations(li, N))
answer = 0
for i in list:
    t = 500
    for j in range(len(i)):
        t += i[j]
        t -= K
        if t < 500:
            answer -=1
            break
    answer += 1

print(answer)


