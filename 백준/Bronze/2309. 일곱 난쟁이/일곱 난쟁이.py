target_list = []

for _ in range(9):
    temp = int(input())
    target_list.append(temp)

cl1 = 0
cl2 = 0

flag = False

for i in range(9):
    if (flag):
        break
    for j in range(i+1, 9):
        sum_ = sum(target_list) - target_list[i] - target_list[j]

        if (sum_ == 100):
            cl1 = i
            cl2 = j
            flag = True
            break

for i in range(9):
    if ((i == cl1) or (i == cl2)):
        target_list[i] = 101

target_list.sort(reverse=False)

for i in range(7):
    print(target_list[i])
