n,m = tuple(map(int, input().split()))
wides = {}
for i in range(n):
    wides[i] = tuple(map(int, input().split()))
wides2 = {}
for i in wides.values():
    for num,j in enumerate(i):
        if num not in wides2:
            wides2[num] = [j]
        else:
            wides2[num].append(j)  
            
answer = 0 
answer += (2 * n*m)

for w in wides.values():
    answer += max(w)
    for ind in range(len(w)-2):
        now_ = w[ind]
        next_ = w[ind+1]
        if now_ > next_:
            plus = min(now_,max(w[ind+2:])) - next_
            if plus >0 :
                answer += plus         

for w in wides.values():
    w = w[::-1]
    answer += max(w)
    for ind in range(len(w)-2):
        now_ = w[ind]
        next_ = w[ind+1]
        if now_ > next_:
            plus = min(now_,max(w[ind+2:])) - next_
            if plus >0 :
                answer += plus
           
for w in wides2.values():
    answer += max(w)
    for ind in range(len(w)-2):
        now_ = w[ind]
        next_ = w[ind+1]
        if now_ > next_:
            plus = min(now_,max(w[ind+2:])) - next_
            if plus >0 :
                answer += plus
           
for w in wides2.values():
    w = w[::-1]
    answer += max(w)
    for ind in range(len(w)-2):
        now_ = w[ind]
        next_ = w[ind+1]
        if now_ > next_:
            plus = min(now_,max(w[ind+2:])) - next_
            if plus >0 :
                answer += plus
print(answer) 

