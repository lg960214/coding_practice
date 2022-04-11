N = int(input())
K = int(input())
t = list(set(map(int, input().split())))
t.sort()
dif = []
for i in range(len(t) - 1):
    dif.append(t[i+1] - t[i])
dif.sort()
print(sum(dif[0:len(dif) - K + 1]))