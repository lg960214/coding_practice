import sys
import math

sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline


class Sol:
    def __init__(self):
        min_, max_ = map(int, input().split())

        array = [0]*(max_-min_+1)
        exp = []

        for i in range(2, int(math.sqrt(max_))+1):
            exp.append(i**2)

        for nn in exp:
            gap = min_ % nn

            if gap == 0:
                idx = gap
            else:
                idx = nn - gap

            while idx <= max_-min_:
                array[idx] = 1
                idx += nn
        

        print(array.count(0))



if __name__ == '__main__':
    user = Sol()