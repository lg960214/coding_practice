target_list = list(map(int, input().split()))

len_set = set(target_list)

if (len(len_set) == 1):
    print(10000 + target_list[0] * 1000)
elif (len(len_set) == 2):
    target = len_set.pop()
    if (target_list.count(target) == 2):
        print(1000 + target * 100)
    else:
        print(1000 + len_set.pop() * 100)
else:
    print(max(target_list) * 100)

