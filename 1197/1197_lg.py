import sys
from collections import defaultdict

sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline

class Sol:
    def __init__(self):
        self.V, self.E = map(int, input().split())
        self.uf = [i for i in range(self.V+1)]
        self.w_list = []
        self.weight = 0

        for i in range(self.E):
            a, b, w = map(int, input().split())
            self.w_list.append([w,a,b])
        
        self.w_list.sort()
        cnt = 0
        
        for info in self.w_list:
            a, b = info[1], info[2]
            uf_a = self.find(a)
            uf_b = self.find(b)

            if uf_a != uf_b:
                self.union(uf_a, uf_b)
                self.weight += info[0]
                cnt += 1
            
            if cnt == self.V-1:
                break
        
        print(self.weight)
        
    def find(self, x):
        if self.uf[x] == x:
            return x
        else:
            return self.find(self.uf[x])

    def union(self, x, y):
        if x < y:
            self.uf[y] = x
        else:
            self.uf[x] = y


if __name__ == '__main__':
    user = Sol()