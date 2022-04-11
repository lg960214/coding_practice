import sys
sys.stdin = open('testcase.txt', 'r')
input = sys.stdin.readline

n = int(input())
k = int(input())
data = list(map(int,input().split()))

if not n == 1:
    if k == 1:
        print(max(data) - min(data))
    else:
        data.sort()

        difference = []
        for i in range(1, len(data)):
            difference.append(data[i]-data[i-1])

        difference.sort()

        print(sum(difference[:-(k-1)]))
else:
    print(0)