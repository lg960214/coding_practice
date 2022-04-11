import sys

sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline


class Sol:
    def __init__(self):
        N = int(input())
        K = int(input())
        sensor = list(map(int, input().split()))

        if K >= N:
            print(0)
        else:
            sensor.sort()
            sub = []
            for i in range(1, N):
                sub.append(sensor[i] - sensor[i-1])

            sub.sort(reverse=True)

            answer = sum(sub[K-1:])

            print(answer)




if __name__ == '__main__':
    user = Sol()