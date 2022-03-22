K, N = map(int, input().split())
len_list = []
for k in range(K):
    len_list.append(int(input()))
left = 0
right = 2 ** 31
max_length = 0
while left < right:
    mid = (left + right) // 2
#     print(left, right, mid)
    count = 0
    for l in len_list:
        count += l // mid
    if count < N:
        right = mid
    elif count >= N:
        left = mid + 1
        max_length = max(max_length, mid)
#     print('-->', left, right, mid, count)

print(max_length)