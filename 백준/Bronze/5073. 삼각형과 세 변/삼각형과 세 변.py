
while True:
    A, B, C = map(int, input().split())

    if (A == B == C == 0):
        break

    if not (A+B > C and A+C > B and B+C > A):
        print('Invalid')
    else:
        if (A==B==C):
            print('Equilateral')
        elif (A==B or B==C or C==A):
            print("Isosceles")
        else:
            print("Scalene")