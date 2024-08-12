number_list = []

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i==j or j==k or k==i: continue
            number_list.append(str(i)+str(j)+str(k))

N = int(input())

for _ in range(N):
    target, s, b = map(str, input().split())

    compare_lst = []

    for comp in number_list:
        s_cnt, b_cnt = 0, 0

        for i in range(3):
            if comp[i] == target[i]:
                s_cnt += 1
            elif target[i] in comp:
                b_cnt += 1

        if s_cnt == int(s) and b_cnt == int(b):
            compare_lst.append(comp)

    number_list = compare_lst

print(len(number_list))