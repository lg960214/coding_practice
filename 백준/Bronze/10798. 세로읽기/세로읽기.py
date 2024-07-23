arr = []

maxl = 0

for i in range(5):
    temp = input()
    arr.append(temp)
    maxl = max(len(temp), maxl)

for i in range(5):
    arr[i] += '_'*(maxl-len(arr[i]))

for i in range(maxl):
    for j in range(5):
        if (arr[j][i] == '_'): continue
        print(arr[j][i], end='')