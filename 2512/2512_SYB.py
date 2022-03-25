N = int(input())
li = list(map(int, input().split()))
li.sort()
max_num = int(input())

answer = 0
for i in range(N):
    if li[i] * (N-i) + sum(li[0:i]) == max_num:
        answer = li[i]
        break
    elif li[i] * (N-i) + sum(li[0:i]) > max_num:
        if i == 0:
            answer = -1
            break
        else:
            n = li[i-1] * (N - i) + sum(li[0:i])
            m = 1
            while n + m * (N - i) <= max_num:
                m += 1
            answer = li[i-1] + m - 1
            break

if answer == 0:
    print(li[-1])
elif answer == -1:
    n = 1
    while n * N <= max_num:
        n += 1
    print(n - 1)
else:
    print(answer)
