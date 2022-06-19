from collections import deque
r,c = map(int, input().split())
graph = []
now_star_list = []
for rr in range(r):
    input_list = list(input())
    new_list = []
    for n, il in enumerate(input_list):
        if il == '.':
            new_list.append(1)
        elif il == 'D':
            new_list.append(1)
            D = rr,n
        elif il == 'S':
            new_list.append(1)
            S = rr,n 
        elif il == '*':
            now_star_list.append([rr,n])
            new_list.append(il)
        else:
            new_list.append(il)
    graph.append(new_list)
def star_bfs(x, y):
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    
    star_list = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if (nx,ny) == D:
            continue
        now_star = graph[nx][ny]
        if now_star in ['X','*'] :
            continue    
        star_list.append((nx,ny)) 
    return star_list
def bfs(x, y):
    global now_star_list
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    
    max_value = 1
    before_max_value = 1
    queue = deque()
    queue.append((x, y))
    star_visited = []
    
    while queue:
        
        if max_value > before_max_value:
            before_max_value = max_value
            new_star_values_list = []
            for nsl in now_star_list:
                new_star_values = star_bfs(nsl[0],nsl[1])
                for nsv in new_star_values:
                    new_star_values_list.append(nsv)
                    graph[nsv[0]][nsv[1]] = '*'
            now_star_list = new_star_values_list    
            

        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx,ny) == D:
                return graph[x][y]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            now = graph[nx][ny]
            now_before = graph[x][y]
      
            if now in ['X','*'] or now_before in ['*'] :
                continue
      
            if graph[nx][ny] == 1:
                next_star_value = now_before + 1
                graph[nx][ny] = next_star_value
                if next_star_value > max_value:
                    max_value = next_star_value
                queue.append((nx, ny))

final_answer = bfs(S[0],S[1])
if type(final_answer) != int:
    print('KAKTUS')
else:
    print(final_answer)
