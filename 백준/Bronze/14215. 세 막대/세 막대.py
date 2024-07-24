A, B, C = map(int, input().split())

if not (A+B > C and A+C > B and B+C > A):
    max_ = max(max(A, B), C)
    print(2*(A+B+C-max_)-1)
else:
    print(A+B+C)
