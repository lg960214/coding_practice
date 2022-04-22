import sys

sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline


class Sol:
    def __init__(self):
        T = int(input())

        for _ in range(T):
            N, K = map(int, input().split())

            target = 0.5*(-1+(1+8*(N/K))**0.5) + 1
            
            if target % 1 == 0:
                ro = int(target)-1
            else:
                ro = int(target)
            

            val_ = 0.5*ro*(ro-1)*K
            if ro % 2 == 0:
                ground = int(ro//2)*K
                direction = 'L'
                answer = int(ground - (N-val_) + 1)
            else:
                ground = -int(ro//2)*K
                direction = 'R'
                answer = int(ground + (N-val_) - 1)

            print(answer, direction)
            
if __name__ == '__main__':
    user = Sol()