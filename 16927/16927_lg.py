import sys
import math


input = sys.stdin.readline

class Sol:
    matrix = list()
    array_dict = dict()
    NM_palindrome = []

    def __init__(self):
        self.N, self.M, self.R = map(int, input().split())
        self.result = [[0]*(self.M) for _ in range(self.N)]

        self.make_palindrome_list()

        for _ in range(self.N):
            temp = list(map(int, input().split()))
            self.matrix.append(temp)

        self.array_generator()


        for i in range(self.N):
            for j in range(self.M):
                num = self.where(i, j)

                how_to_rotate = self.array_dict[num]

                target = how_to_rotate.index((i, j)) + self.R

                x, y = how_to_rotate[target%len(how_to_rotate)]
                
                self.result[x][y] = self.matrix[i][j]

        for answer in self.result:
            for ans in answer:
                print(ans, end= ' ')
            print()

    def make_palindrome_list(self):
        temp = [self.N / 2, self.M / 2]
        
        for factor in temp:
            if factor % 1 == 0:
                factor = int(factor)
                palin_ = [i for i in range(1, factor+1)]
                for j in range(0, factor):
                    j = factor - j
                    palin_.append(j)
            else:
                factor = math.ceil(factor)
                palin_ = [i for i in range(1, factor+1)]
                for j in range(1, factor):
                    j = factor - j
                    palin_.append(j)

            self.NM_palindrome.append(palin_)



    def where(self, idx_1, idx_2):
        a = idx_1
        b = idx_2
        a = self.NM_palindrome[0][a]
        b = self.NM_palindrome[1][b]

        return min(a, b)

    
    def array_generator(self):
        for key in range(1, int(min(self.N, self.M)/2)+1):
            std_a = self.N - 2*key + 1
            std_b = self.M - 2*key + 1

            x_ = 0 + (key-1)
            y_ = 0 + (key-1)

            temp_ = list()

            for _ in range(std_a):
                x_ += 1
                temp_.append((x_, y_))

            for _ in range(std_b):
                y_ += 1
                temp_.append((x_, y_))

            for _ in range(std_a):
                x_ -= 1
                temp_.append((x_, y_))

            for _ in range(std_b):
                y_ -= 1
                temp_.append((x_, y_))
                            
            self.array_dict[key] = temp_



if __name__ == '__main__':
    user = Sol()