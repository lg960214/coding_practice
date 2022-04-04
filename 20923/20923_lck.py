import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

do, su = deque([]), deque([])
for _ in range(n):
    a, b = map(int, input().split())
    do.append(a)
    su.append(b)

do_ground = deque([0])
su_ground = deque([0])

for i in range(m):
    if not i % 2:
        do_ground.append(do.pop())

        if not do:
            print("su")
            break
        if do_ground[-1] == 5:
            # 도도 승
            su_ground.popleft()
            do_ground.popleft()
            do.extendleft(su_ground)
            do.extendleft(do_ground)
            do_ground = deque([-1])
            su_ground = deque([-1])
        elif do_ground[-1] + su_ground[-1] == 5:
            # 수연 승
            su_ground.popleft()
            do_ground.popleft()
            su.extendleft(do_ground)
            su.extendleft(su_ground)
            do_ground = deque([-1])
            su_ground = deque([-1])

    else:
        su_ground.append(su.pop())

        if not su:
            print("do")
            break
        if su_ground[-1] == 5:
            # 도도 승
            su_ground.popleft()
            do_ground.popleft()
            do.extendleft(su_ground)
            do.extendleft(do_ground)
            do_ground = deque([-1])
            su_ground = deque([-1])
        elif do_ground[-1] + su_ground[-1] == 5:
            # 수연 승
            su_ground.popleft()
            do_ground.popleft()
            su.extendleft(do_ground)
            su.extendleft(su_ground)
            do_ground = deque([0])
            su_ground = deque([0])
else:
    if len(do) > len(su):
        print("do")
    elif len(do) < len(su):
        print("su")
    else:
        print("dosu")
