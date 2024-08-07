import sys
from collections import deque

input = sys.stdin.readline

class My_sol:
    max_ = 0
    tf = True
    
    def __init__(self):
        self.N = int(input())
        self.num_list = list(map(int, input().split()))
        self.p = [0]*(self.N + 1)
    
    def DFS(self, l, p):
        
        if self.tf == True:
            cnt_list = [0]*(self.N+1)
            self.tf = False
        else:
            cnt_list = p
        
        list_ = l
        
        
        if len(list_) == self.N:
            sum_ = 0
            for i in range(self.N-1):
                sum_ += abs(list_[i] - list_[i+1])
            self.max_ = max(sum_, self.max_)
        else:
            for i in range(self.N):
                if cnt_list[i] == 0:
                    cnt_list[i] = 1
                    list_.append(self.num_list[i])
                    self.DFS(list_, cnt_list)
                    del list_[sum(cnt_list)-1]
                    cnt_list[i] = 0

user = My_sol()
user.DFS([], [])
print(user.max_)