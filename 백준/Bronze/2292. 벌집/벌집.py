N = int(input())

prev = 1
for i in range(1, 100000):
    target = 3*i*(i-1) + 2
    if (prev <= N < target):
        print(i)
        break
    prev = target