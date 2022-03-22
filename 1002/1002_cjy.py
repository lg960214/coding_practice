T = int(input())

for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif abs(r1 - r2) == d or (r1 + r2) == d:
        print(1)
    elif abs(r1 - r2) > d or (r1 + r2) < d:
        print(0) 
    else:
        print(2)
