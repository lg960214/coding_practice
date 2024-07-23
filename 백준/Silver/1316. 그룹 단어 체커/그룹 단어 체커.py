N = int(input())

ans = 0

for i in range(N):
    target = input() + '0'
    temp = ''
    prev = ''
    for i in range(len(target)):
        if (i == 0):
            prev = target[i]
        else:
            if (prev == target[i]):
                pass
            else:
                temp += prev
                prev = target[i]

    target = temp

    dict_ = dict()
    flag = False
    for i in range(len(target)):
        if (dict_.get(target[i]) == None):
            dict_[target[i]] = 0
        else:
            flag = True
            break
    if not (flag):
        ans += 1

print(ans)