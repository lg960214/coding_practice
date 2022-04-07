import sys
from collections import deque, defaultdict

input = sys.stdin.readline


class Sol:
    def __init__(self):
        self.N, self.S, self.M = map(int, input().split())
        self.V = deque(list(map(int, input().split())))
        self.find = defaultdict(int)
        self.find[self.S] = 1 
        answer = list()

        append = 0

        for i in range(self.N):
            pm = self.V.popleft()

            keys_list = list(self.find.keys())
            self.find = defaultdict(int)

            for key in keys_list:
                target = key
                if 0 <= target-pm <= self.M:
                    self.find[target-pm] = 1
                if 0 <= target+pm <= self.M:
                    self.find[target+pm] = 1

        answer = list(self.find.keys())

        if len(answer) > 0:
            print(max(answer))
        else:
            print(-1)
        

if __name__ == '__main__':
    user = Sol()