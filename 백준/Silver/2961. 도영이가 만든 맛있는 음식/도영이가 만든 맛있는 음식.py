def dfs(step, idx, S_sm, B_sm):
    global ans

    if step > N:
        return
    
    if (step >= 1):
        ans = min(abs(B_sm - S_sm), ans)
        
    for i in range(idx, N):
        S_sm = S_sm * ingredients[i][0]
        B_sm = B_sm + ingredients[i][1]
        dfs(step+1, i+1, S_sm, B_sm)
        S_sm = S_sm // ingredients[i][0]
        B_sm = B_sm - ingredients[i][1]

N = int(input())
visit = [False]*N

ingredients = [list(map(int, input().split())) for _ in range(N)]
visit[0] = True

ans = 1e9
dfs(0, 0, 1, 0)
print(ans)