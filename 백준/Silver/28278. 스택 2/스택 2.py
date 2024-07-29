import sys

input = sys.stdin.readline

N = int(input())

stack_ = []

for _ in range(N):
    temp = input().rstrip().split()
    if (len(temp) == 2):
        stack_.append(temp[1])
    else:
        if (temp[0] == '2'):
            if (len(stack_) != 0):
                print(stack_.pop())
            else:
                print(-1)
        if (temp[0] == '3'):
            print(len(stack_))
        if (temp[0] == '4'):
            if (len(stack_) == 0):
                print(1)
            else:
                print(0)
        if (temp[0] == '5'):
            if (len(stack_) != 0):
                print(stack_[-1])
            else:
                print(-1)