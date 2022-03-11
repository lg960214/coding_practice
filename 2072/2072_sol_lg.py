import sys
import copy
from collections import deque


input = sys.stdin.readline

class Renju:
    def __init__(self):
        self.N = int(input())
        self.board = [[0]*(20) for _ in range(20)]
        self.answer = 0
        self.black = deque()
        self.white = deque()
        self.method = [[(-1,0),(1,0)],
                        [(0,-1),(0,1)],
                        [(-1,1),(1,-1)],
                        [(-1,-1),(1,1)]]
        for _ in range(self.N):
            x, y = map(int, input().split())
            if _ % 2 == 0:
                self.black.append((x, y))
            else:
                self.white.append((x, y))
    
        self.order = [None, self.black, self.white]

    def placement(self):
        ass = 2
        while (self.black and self.white):
            self.answer += 1

            if ass == 2:
                ass = 1
            else:
                ass = 2
            
            order = self.order[ass]
            x, y = order.popleft()
            self.board[x][y] = ass

            re = self.search()

            if re == 1:
                return self.answer
            else:
                pass
        return -1

    def search(self):
        self.test = copy.deepcopy(self.board)
        a, b, c, d = 0, 0, 0, 0
        
        for bw in range(1, 3):
            for i in range(1, 20):
                for j in range(1, 20):
                    if self.board[i][j] == bw:
                        a = self.gr(i, j, bw, 0)
                        b = self.gr(i, j, bw, 1)
                        c = self.gr(i, j, bw, 2)
                        d = self.gr(i, j, bw, 3)
                    if (a == 5) or (b == 5) or (c == 5) or (d == 5):
                        return 1
        return -1

    def gr(self, x, y, bw, me):
        count = 1
        search_queue = deque([(x,y)])
        dx, dy = self.method[me][0]

        while search_queue:
            x1, y1 = search_queue.popleft()
            try:
                if self.board[x1+dx][y1+dy] == bw:
                    count += 1
                    search_queue.append((x1+dx, y1+dy))
            except:
                break

        search_queue = deque([(x,y)])
        dx, dy = self.method[me][1]

        while search_queue:
            x1, y1 = search_queue.popleft()
            try:
                if self.board[x1+dx][y1+dy] == bw:
                    count += 1
                    search_queue.append((x1+dx, y1+dy))
            except:
                break
        
        return count


if __name__ == '__main__':
    user = Renju()
    result = user.placement()
    print(result)