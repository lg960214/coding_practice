import sys
from collections import defaultdict

sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline


class Sol:
    cost = []
    client = []

    def __init__(self):
        self.C, self.N = map(int, input().split())
        self.knapsack = [[0 for _ in range(self.C*100+1)] for _ in range(self.N+1)]

        for _ in range(self.N):
            a, b = map(int, input().split())
            self.cost.append(a)
            self.client.append(b)
        
        for i in range(1, self.N+1):
            cost_ = self.cost[i-1]
            client_ = self.client[i-1]
            for j in range(1, self.C*100+1):
                if j < cost_:
                    self.knapsack[i][j] = self.knapsack[i-1][j]
                else:
                    target = max(self.knapsack[i-1][j-cost_] + client_, 
                    self.knapsack[i][j-cost_] + client_,
                    self.knapsack[i-1][j])
                    self.knapsack[i][j] = target
        
        for __ in self.knapsack:
            print(__[290:310])

        for factor in self.knapsack[self.N]:
            if factor >= self.C:
                target = self.knapsack[self.N].index(factor)
                print(target)
                break
        
if __name__ == '__main__':
    user = Sol()