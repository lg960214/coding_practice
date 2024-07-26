M, N = map(int, input().split())
T = int(input())

x_lst = [0, N]
y_lst = [0, M]

for _ in range(T):
    case, num = map(int, input().split())

    if (case == 0):
        x_lst.append(num)
    else:
        y_lst.append(num)
x_lst.sort()
y_lst.sort()

mx = 0
my = 0
for i in range(1, len(x_lst)):
    mx = max(mx, x_lst[i] - x_lst[i-1])
for i in range(1, len(y_lst)):
    my = max(my, y_lst[i] - y_lst[i-1])

print(mx*my)