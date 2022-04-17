import sys


sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline


class Sol:

    def __init__(self):
        list_ = []

        self.value = list(map(int, input().split()))
        self.value.sort()


        for val in self.value:
            floor = int((val-1)**0.5) + 1 # 몇 층에 있는 지

            loc_1 = int(((floor-1)**2 + 1 + floor**2)/2)
            loc_1 = val-loc_1 # 중앙으로부터의 위치 표시

            if floor%2 == loc_1%2: # 해당 숫자 위치의 삼각형 모양
                loc_2 = '역삼각형'
            else:
                loc_2 = '정삼각형'

            list_.append([floor, loc_1, loc_2])


        gap = 0 # 움직여야 하는 이동 횟수 정의

        if list_[0][0] == list_[1][0]: # 같은 층에 있을 때 
            gap = list_[1][1]-list_[0][1]
        else:
            if list_[0][2] == '역삼각형':
                gap += 1
            if list_[1][2] == '역삼각형':
                gap -= 1

            sub = list_[1][0] - list_[0][0] # 두 숫자의 층 차이
            gap += 2*(list_[1][0] - list_[0][0]) # 층마다 2번씩 이동

            if list_[0][1] - sub <= list_[1][1] <= list_[0][1] + sub: # 예외 처리
                pass
            elif list_[1][1] < list_[0][1] - sub:
                gap += list_[1][1] - (list_[0][1]-sub)
            else:
                gap += (list_[0][1]+sub) - list_[1][1]

        
        print(gap)
        

if __name__ == '__main__':
    user = Sol()