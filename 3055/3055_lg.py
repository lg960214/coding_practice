import sys
from collections import deque



sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline


class Sol:
    matrix = []
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    assignment = False
    time = []

    def __init__(self):
        self.R, self.C = map(int, input().split())

        for _ in range(self.R):
            temp = list(input().rstrip())
            self.matrix.append(temp)
        
        self.visit = [[-1 for i in range(self.C)] for i in range(self.R)]


        # 각 위치 탐색
        self.start = ''
        self.end = ''
        flood = []

        for i in range(self.R):
            for j in range(self.C):
                target = self.matrix[i][j]

                if target == 'D':
                    self.end = [i, j]
                elif target == 'S':
                    self.start = [i, j]
                elif target == '*':
                    self.matrix[i][j] = 0
                    flood.append([i, j])

        for __ in self.matrix:
            print(__)

        self.BFS_flood(flood)
        print('----------------')
        for __ in self.matrix:
            print(__)
        self.Escape()

        if self.assignment == True:
            print(min(self.time))
        else:
            print('KAKTUS')


    def BFS_flood(self, flood):
        start_node = flood

        for list_ in start_node:
            queue = deque([list_])
            cnt = 1

            while queue:
                temp_queue = []

                while queue:
                    target = queue.popleft()
                    x, y = target[0], target[1]

                    for i in range(4):
                        x_1 = x + self.dx[i]
                        y_1 = y + self.dy[i]

                        if (0 <= x_1 < self.R) and (0 <= y_1 < self.C):
                            if self.matrix[x_1][y_1] == '.':
                                self.matrix[x_1][y_1] = cnt
                                temp_queue.append([x_1, y_1])

                            elif type(self.matrix[x_1][y_1]) == type(1):
                                if self.matrix[x_1][y_1] > cnt:
                                    self.matrix[x_1][y_1] = cnt
                                    temp_queue.append([x_1, y_1])

                queue.extend(temp_queue)
                cnt += 1


    def Escape(self):
        queue = deque([self.start])

        step = 1

        while queue:
            temp_queue = []
            
            while queue:
                target = queue.popleft()
                x, y = target[0], target[1]

                for i in range(4):
                    x_1 = x + self.dx[i]
                    y_1 = y + self.dy[i]

                    if (0 <= x_1 < self.R) and (0 <= y_1 < self.C):
                        if [x_1, y_1] == self.end:
                            self.assignment = True
                            self.time.append(step)
                            break

                        if type(self.matrix[x_1][y_1]) == type(1):
                            if self.matrix[x_1][y_1]  > step:
                                temp_queue.append([x_1, y_1])

                        elif self.matrix[x_1][y_1] == '.':
                            temp_queue.append([x_1, y_1])
                            
                        self.matrix[x_1][y_1] = -1

            queue.extend(temp_queue)
            step += 1



            
if __name__ == '__main__':
    user = Sol()