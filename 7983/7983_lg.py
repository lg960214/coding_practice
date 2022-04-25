import sys


sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline


class Sol:
    def __init__(self):
        N = int(input())
        list_ = []

        for _ in range(N):
            d, t = map(int, input().split())
            list_.append([t, d])
        
        list_.sort(reverse=True)

        target = list_[0][0]

        for i in range(N):
            due = list_[i][0]
            length = list_[i][1]

            if target >= due:
                target = due - length
            else:
                target = target - length
        
        print(target)


        
if __name__ == '__main__':
    user = Sol()