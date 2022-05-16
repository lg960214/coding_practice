pu = []
for _ in range(12):
    pu.append(list(input()))
    
def check(a,x,y):
    if x != 0:
        if [x-1,y] not in checked_list and pu[x-1][y] == a:
            checked_list.append([x-1,y])
            check(a,x-1,y)
    if x != 11:
        if [x+1,y] not in checked_list and pu[x+1][y] == a:
            checked_list.append([x+1,y])
            check(a,x+1,y)
    if y != 0:
        if [x,y-1] not in checked_list and pu[x][y-1] == a:
            checked_list.append([x,y-1])
            check(a,x,y-1)
    if y != 5:
        if [x,y+1] not in checked_list and pu[x][y+1] == a:
            checked_list.append([x,y+1])
            check(a,x,y+1)
    return 

already = []
checked_list = []
puyo_list = []
answer = 0

while True:
    for i in range(12):
        for j in range(6):
            if [i,j] in already:
                continue
            now = pu[i][j]
            if now != '.':
                check(now,i,j)
            else:
                continue
            if checked_list:
                if len(checked_list) >= 4:
                    puyo_list.extend(checked_list)
                already.extend(checked_list)
                checked_list = []
    if not puyo_list:
        break
    else:
        answer += 1
        puyo_dict = {}
        for p in puyo_list:
            r = p[0]
            c = p[1]
            if c not in puyo_dict:
                puyo_dict[c] = [r]
            else:
                puyo_dict[c] += [r]
        for i in puyo_dict:
            one_puyo = puyo_dict[i]
            len_i = len(one_puyo)
            new_one_puyo = []
            for k in range(max(one_puyo)+1):
                if k in one_puyo:
                    continue
                new_one_puyo.append(pu[k][i])
            for k in range(max(one_puyo),len_i-1,-1):
                pu[k][i] = new_one_puyo.pop()
            for l in range(len_i):
                pu[l][i] = '.'
        already = []
        checked_list = []
        puyo_list = []

print(answer)