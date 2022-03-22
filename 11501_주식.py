n = int(input())
for _ in range(n):
    q = int(input())
    a = tuple(map(int, input().split()))
    answer = 0
    pre_n = a[-1]
    number = len(a) - 1
    for i in range(len(a)-2,-1,-1):
        if a[i]>=pre_n:
            answer += ((number-(i+1)) * pre_n - sum(a[i+1:number]))
            number = i
            pre_n = a[number]
        if i == 0 and pre_n != a[0]:
            answer += (number * pre_n - sum(a[:number]))  
    print(answer)     

