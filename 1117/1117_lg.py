import sys

sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline


class Sol:
    def __init__(self):
        W, H, f, c, x1, y1, x2, y2 = map(int, input().split(' '))

        # 접기

        W_1 = max(W-f, f) # 변의 길이
        W_2 = min(W-f, f) # 겹쳐지는 변의 수
        H_1 = int(H/(c+1)) # 높이 
        H_2 = c+1 # 겹쳐지는 높이 수

        answer = 0

        if x2 <= W_2:
            answer += 2*(x2-x1)
        elif x1 <= W_2 < x2:
            answer += (x2-W_2) + 2*(W_2 - x1)
        else:
            answer += x2-x1

        answer = H_2*(y2-y1)*answer
        
        print(H*W-answer)





if __name__ == '__main__':
    user = Sol()