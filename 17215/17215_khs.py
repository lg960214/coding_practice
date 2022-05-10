a = input()

answer = []
ind = 0

def score(x):
    if x == 'S':
        return 10
    elif x == 'P':
        return 10
    elif x == '-':
        return 0
    else:
        return int(x)

for i in range(len(a)):
    now = a[i]
    if now == 'S':
        if a[i+2] != 'P':
            answer.append((10 + score(a[i+1])+score(a[i+2])))
        else:
            answer.append(20)
        ind += 1
    elif now == 'P':
        answer[ind] = (10 + score(a[i+1]))
        ind += 1
    else:
        if len(answer) == ind:
            answer.append(score(now))
        else:
            answer[ind] += score(now)
            ind += 1
    if ind == 10:
        break  
print(sum(answer))

