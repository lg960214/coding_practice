import sys
from collections import deque

sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline


class Sol:

    def __init__(self):
        start = []
        end = []
        timestamp = []

        N = int(input())

        for _ in range(N):
            num, s, e = map(int, input().split())
            start.append(s)
            end.append(e)
            timestamp.append(s)
            timestamp.append(e)

        start.sort(reverse=False)
        end.sort(reverse=False)
        timestamp.sort(reverse=False)

        start = deque(start)
        end = deque(end)
        timestamp = deque(timestamp)

        count = 0
        max_ = 0

        comp_1 = start.popleft()
        comp_2 = end.popleft()
        assignment = True

        
        while assignment:
            if not start:
                assignment = False

            target = timestamp.popleft()

            if target == comp_1:
                if target == comp_2:
                    if assignment:
                        comp_1 = start.popleft()
                        comp_2 = end.popleft()
                        timestamp.popleft()
                    else:
                        pass
                else:
                    count += 1
                    if assignment:
                        comp_1 = start.popleft()
                    else:
                        pass
            elif target == comp_2:
                count -= 1
                if assignment:
                    comp_2 = end.popleft()
                else:
                    pass

            max_ = max(max_, count)

            

        print(max_)



if __name__ == '__main__':
    user = Sol()