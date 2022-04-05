import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    hints = list(map(int, input().strip()))
    boards = input()
    result = sum(hints)
    if hints[0]:
        result += 1
    if hints[-1]:
        result += 1
    print(result // 3)
