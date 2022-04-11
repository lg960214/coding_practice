n = int(input())
needs = tuple(map(int, input().split()))
total = int(input())
r = max(needs)
l = 0
now_n = r // 2
if sum(needs) <= total:
    print(r)
else:
    while l <= r:
        sum_needs = 0
        for i in needs:
            if i >= now_n:
                sum_needs += now_n
            else:
                sum_needs += i       
        if sum_needs <= total:
            l = now_n + 1
        else:
            r = now_n - 1
        now_n = (l+r) // 2
    print(now_n)   

