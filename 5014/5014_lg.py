import sys
from collections import defaultdict

sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline


class Sol:

    def __init__(self):
        F, S, G, U, D = map(int, input().split())

        visit = defaultdict(int)
        assignment = True
        count = 0

        while True:
            visit[S] = 1
            print(S)
            if S < G:
                if S + U <= F:
                    if visit[S+U] == 0:
                        S += U
                    else:
                        assignment = False
                        break
                else:
                    if S - D >= 1:
                        if visit[S-D] == 0:
                            S -= D
                        else:
                            assignment = False
                            break
                    else:
                        assignment = False
                        break
                    
            elif S > G:
                if S - D >= 1:
                    if visit[S-D] == 0:
                        S -= D
                    else:
                        assignment = False
                        break
                else:
                    if S + U <= F:
                        if visit[S+U] == 0:
                            S += U
                        else:
                            assignment = False
                            break
                    else:
                        assignment = False
                        break
            
            else:
                break
            count += 1
        print('------------')
        if assignment == True:
            print(count)
        else:
            print('use the stairs')






        
if __name__ == '__main__':
    user = Sol()