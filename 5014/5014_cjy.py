import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
floors = [[-1, -1]]
for i in range(1, F + 1):
    tmp = []
    if i - D >= 1:
        tmp.append(i - D)
    if i + U <= F:
        tmp.append(i + U)
    floors.append(tmp)

queue = deque([S])
distance = [-1] * (F + 1)
distance[S] = 0
while queue:
    now = queue.popleft()
    choices = floors[now]
    for choice in choices:
        if distance[choice] == -1: # not visited
            queue.append(choice)
            distance[choice] = distance[now] + 1
            if choice == G:
                queue = []
                break
if distance[G] != -1:
    print(distance[G])
else:
    print('use the stairs')
