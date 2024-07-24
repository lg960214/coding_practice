T = int(input())
a = [[0]*103 for _ in range(103)]
minnx = 102
minny = 102
maxxx = -1
maxxy = -1
for _ in range(T):
    c,b = map(int,input().split())
    for i in range(c+1,c+11):
        for j in range(b+1,b+11):
            a[i][j] = 1
    # minnx = min(minnx,c+1)
    # minny = min(minny,b+1)
    # maxxx = max(maxxx,c+11)
    # maxxy = max(maxxy,b+11)
summ = 0

for i in range(0, 103):

    for j in range(0,103):
        if(a[i][j] == 0): continue

        if a[i][j-1] == 0:
            summ+=1
            #a[i][j] = 3
        if a[i][j+1] == 0:
            summ+=1
            #a[i][j] = 3
        if a[i-1][j] == 0:
            summ+=1
            #a[i][j] = 3
        if a[i+1][j] == 0:
            summ+=1
            #a[i][j] = 3

print(summ)