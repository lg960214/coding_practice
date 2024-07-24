N = int(input())

target_list = list(map(int, input().split()))
ans = 0

for i in range(0, N):
    target_b = target_list[i]
    cnt = 0
    gradient = 1e9
    for j in range(i-1, -1, -1):
        # (j, l[j]) 에서 (i, l[i])로
        temp_gradient = (target_list[i] - target_list[j]) / (i-j)
        if (gradient > temp_gradient):
            gradient = temp_gradient
            cnt += 1
        else:
            pass

    gradient = -1e9
    for j in range(i+1, N):
        temp_gradient = (target_list[j] - target_list[i]) / (j-i)
        if (gradient < temp_gradient):
            gradient = temp_gradient
            cnt += 1
        else:
            pass

    ans = max(ans, cnt)

print(ans)