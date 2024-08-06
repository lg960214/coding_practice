import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline


class Sol:
    matrix = []
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    def __init__(self):
        
        for _ in range(12):
            temp = list(input().rstrip())
            self.matrix.append(temp)
        
        self.column_length = len(self.matrix)
        self.row_length = len(self.matrix[0])

        cnt = 1
        step = 0

        while cnt:
            cnt = self.BFS()
            if cnt == 0:
                break

            step += 1

        print(step)



    def BFS(self):
        visit_node = [[0 for i in range(self.row_length)] for j in range(self.column_length)]
        count = 0
        loc_list = []

        for i in range(self.column_length):
            for j in range(self.row_length):

                if visit_node[i][j] == 0:
                    visit_node[i][j] = 1
                    target = self.matrix[i][j]

                    if target != '.':
                        num_of_blocks = 1
                        queue = deque([[i, j]])
                        temp_loc_list = [[i, j]]

                        while queue:
                            loc = queue.popleft()
                            x, y = loc[0], loc[1]

                            for d in range(4):
                                x_ = x + self.dx[d]
                                y_ = y + self.dy[d]
                                if (0 <= x_ < self.column_length) and (0 <= y_ < self.row_length):
                                    if (self.matrix[x_][y_] == target) and (visit_node[x_][y_] == 0):
                                        queue.append([x_, y_])
                                        temp_loc_list.append([x_, y_])
                                        visit_node[x_][y_] = 1
                                        num_of_blocks += 1



                    else:
                        num_of_blocks = 0
                    
                    if num_of_blocks >= 4:
                        count += 1
                        loc_list = loc_list + temp_loc_list


        for locations in loc_list:
            x, y = locations[0], locations[1]
            self.matrix[x][y] = '.'
        

        for locations in loc_list:
            x, y = locations[0], locations[1]
            for k in range(x, -1, -1):
                self.matrix[k][y] = self.matrix[k-1][y]
            self.matrix[0][y] = '.'


        return count




if __name__ == '__main__':
    user = Sol()