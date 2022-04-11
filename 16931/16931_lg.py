import sys

input = sys.stdin.readline

class Sol:
    matrix = []

    def __init__(self):
        self.N, self.M = map(int, input().split())
        
        for _ in range(self.N):
            temp = list(map(int, input().split()))
            self.matrix.append(temp)
        

        # Top
        count_up = self.N*self.M

        # Side
        count_side = 0

        for i in range(self.N):
            for j in range(self.M):
                if j == 0:
                    count_side += self.matrix[i][j]
                    prev = self.matrix[i][j]
                else:
                    count_side += max(self.matrix[i][j] - prev, 0)
                    prev = self.matrix[i][j]
        
        # Front

        count_front = 0
        prev = [0]*self.M

        for i in range(self.N):
            for j in range(self.M):
                if i == 0:
                    count_front += self.matrix[i][j]
                    prev[j] = self.matrix[i][j]
                else:
                    count_front += max(self.matrix[i][j]-prev[j], 0)
                    prev[j] = self.matrix[i][j]

        answer = 2*(count_up + count_side + count_front)

        print(answer)

if __name__ == '__main__':
    user = Sol()
