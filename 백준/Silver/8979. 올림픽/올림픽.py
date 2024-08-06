N, K = map(int, input().split())

target_lst = ''
arr = []

for _ in range(N):
    temp_lst = list(map(int, input().split()))
    if temp_lst[0] == K:
        target_lst = temp_lst
    arr.append(temp_lst)

rank = 1

for i in range(N):
    comp_lst = arr[i]
    if comp_lst[1] > target_lst[1]:
        rank += 1
    elif comp_lst[1] == target_lst[1]:
        if comp_lst[2] > target_lst[2]:
            rank += 1
        elif comp_lst[2] == target_lst[2]:
            if comp_lst[3] > target_lst[3]:
                rank += 1

print(rank)

