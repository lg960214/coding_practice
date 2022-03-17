import sys
from collections import deque


input = sys.stdin.readline

class Sol:
    nadori_list = []
    step = 0
    ass = True

    def __init__(self):
        self.N, self.K, self.T = map(int, input().split())
        self.nadori_list = list(map(int, input().split()))

        self.nadori_list.sort(reverse=True)
        self.nadori_queue = deque(self.nadori_list)

        self.cal()


    def cal(self):
        residue = 0
        sum_ = sum(self.nadori_queue)

        if (sum_ % self.K != 0):
            print('NO')
            return
            
        if sum_ == 0:
            print("YES")
            return
        
        while self.nadori_queue:
            if residue == 0:
                left = self.nadori_queue.popleft()
                residue = self.discriminate(left)
            
            else:
                left = self.nadori_queue.popleft()
                residue = self.discriminate(left, residue)

            if residue == 'finish':
                return

        if self.ass == True:
            print('YES')

    def discriminate(self, l, r=0):
        left = l
        right = r
        gap = self.K - left

        while gap:

            if right == 0:
                right = self.nadori_queue.pop()


            if gap > right:
                self.step += right
                gap -= right
                right = 0
            elif gap == right:
                self.step += right
                gap = 0
                right = 0
            else:
                self.step += gap
                right -= gap
                gap = 0


            if self.step > self.T:
                self.ass = False
                print('NO')
                return 'finish'

        return right



if __name__ == '__main__':
    user = Sol()