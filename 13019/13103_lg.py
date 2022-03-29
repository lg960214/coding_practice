import sys

input = sys.stdin.readline

class Sol:
    move = 0
    
    def __init__(self):
        self.A = input().rstrip() # AABCASDD
        self.B = input().rstrip() # BACASADD

        set_A = set(self.A)
        set_B = set(self.B)

        for factor in set_A:
            if self.A.count(factor) != self.B.count(factor):
                print(-1)
                return
        
        self.cal()


    def cal(self):
        end = 0

        for i in range(1, len(self.A)+1):
            if self.A[-i] == self.B[-i]:
                end += 1
            else:
                break
        
        if end > 0:
            self.A = self.A[:-end]
            self.B = self.B[:-end]

        if len(self.A) == 0:
            print(0)
            return

        k = 1
        idx = 0

        while True:
            idx = self.A.rfind(self.B[-k])
            if idx == -1:
                break
            
            self.A = self.A[:idx]
            
            k += 1
        
        print(len(self.B)-k+1)




if __name__ == '__main__':
    user = Sol()