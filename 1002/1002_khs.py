import sys 
N = int(sys.stdin.readline()) 
for i in range(N): 
    x1,y1,r1,x2,y2,r2 = list(map(int, sys.stdin.readline().split()))
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        distance = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
        r_distance = r1 + r2
        r_distance2 = abs(r1 - r2)
        if distance == r_distance:
            print(1)
        elif distance == r_distance2:
            print(1)
        elif r_distance2 > distance:
            print(0)
        elif r_distance < distance:
            print(0)
        else:
            print(2)

