import sys

sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline


class Sol:

    def __init__(self):
        H, W = map(int, input().split())
        matrix = []
        half = 0
        one = 0
        
        for _ in range(H):
            assignment = False
            temp = list(map(str, input().rstrip()))
            for factor in temp:
                if (factor == '/') or (factor == '\\'):
                    if assignment == False:
                        assignment = True
                        half += 0.5
                    else:
                        assignment = False
                        half += 0.5
                elif factor == '.':
                    if assignment == True:
                        one += 1
        
        print(int(half + one))




if __name__ == '__main__':
    user = Sol()