import sys
from collections import deque

input = sys.stdin.readline

class Sol:
    def __init__(self):
        N, r, c = map(int, input().split())
        idx_list = []
        

        r += 1
        c += 1        
        num= N-1
        self.threshold_r = 2**num
        self.threshold_c = 2**num

        for _ in range(N):
            if self.threshold_r < r:
                if self.threshold_c < c:
                    idx_list.append(4)
                    self.cal(4, num)
                else:
                    idx_list.append(3)
                    self.cal(3, num)


            else:
                if self.threshold_c < c:
                    idx_list.append(2)
                    self.cal(2, num)
                else:
                    idx_list.append(1)
                    self.cal(1, num)
            num -= 1

        idx_list = deque(idx_list)
        count = 1
        k = 0
        
        while idx_list:
            target = idx_list.pop()
            target = (target-1)*(2**k)
            count += target
            k += 2
        print(count-1)



    def cal(self, number, thr):
        if number == 4:
            self.threshold_r += 2**(thr-1)
            self.threshold_c += 2**(thr-1)
        elif number == 3:
            self.threshold_r += 2**(thr-1)
            self.threshold_c -= 2**(thr-1)
        elif number == 2:
            self.threshold_r -= 2**(thr-1)
            self.threshold_c += 2**(thr-1)
        else:
            self.threshold_r -= 2**(thr-1)
            self.threshold_c -= 2**(thr-1)
        return



if __name__ == '__main__':
    user = Sol()