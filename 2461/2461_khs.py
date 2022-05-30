n,m = list(map(int, input().split()))
classes = []
for _ in range(n):
    classes.append(sorted(list(map(int, input().split()))))

full = []
class_dic = {}
for num,c in enumerate(classes):
    for j in c:
        full.append(j)
        if j not in class_dic:
            class_dic[j] = [num]
        else:
            class_dic[j] += [num]
full = sorted(full)

max_values = []
for i in classes:
    max_values.append(i[0])
answer = 1000000000
pre_f = -1
for f in full:
    if f == pre_f and class_dic[f]:
        if not class_dic[f] : 
            continue
        mv_ind = class_dic[f].pop(0)
        classes[mv_ind].pop(0)
    if not class_dic[f] : 
        continue
    mv_ind = class_dic[f].pop(0)
    if len(classes[mv_ind]) != 1:
        classes[mv_ind].pop(0)
    now_max = max(max_values)
    now_min = min(max_values)
    now_answer = now_max - now_min
    if now_answer < answer:
        answer = now_answer
    if not classes[mv_ind] : 
        continue   
    max_values[mv_ind] = classes[mv_ind][0]
    
    pre_f = f
print(answer)