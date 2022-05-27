import sys
sys.setrecursionlimit(10**6)
m, n = list(map(int, input().split()))
h = []
for _ in range(m):
    h.append(list(map(int, input().split())))
answer = 0

bag = []
for i in range(m):
    bag.append([0]*n)
    
def bfs(r,c):
    for next_ in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
        next_r = r + next_[0]
        next_c = c + next_[1]
        if next_r >= 0 and next_r < m and next_c >= 0 and next_c < n  and bag[next_r][next_c] == 0:
            bag[next_r][next_c] = 1
            if  h[next_r][next_c] == 1:
                bfs(next_r,next_c)
    return 

for i in range(m):
    for j in range(n):
        if bag[i][j] == 0:
            if h[i][j] == 1:
                answer += 1
                bag[i][j] = 1
                bfs(i,j)
            else:
                bag[i][j] = 1

print(answer)