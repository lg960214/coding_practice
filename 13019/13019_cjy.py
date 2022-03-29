import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

if sorted(A) != sorted(B):
    count = -1
    print(count)
else:
    count = 0
    a, b = len(A) - 1, len(B) - 1
    while a >= 0 and b >= 0:
        if A[a] == B[b]:
            b -= 1
            count += 1
        a -= 1

    print(len(A) - count)
