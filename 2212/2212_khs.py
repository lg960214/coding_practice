n = int(input())
k = int(input())
sensors = sorted(tuple(map(int, input().split())))
if k == 1:
    print(max(sensors)-min(sensors))
else:    
    minus = []
    for i in range(len(sensors)-1):
        minus.append(sensors[i+1]-sensors[i])

    print(sum(sorted(minus)[:-(k-1)]))

