h, m = map(int, input().split())
t = int(input())

t_h = t // 60
t_m = t % 60

h += t_h
m += t_m

if (m >= 60):
    m -= 60
    h += 1

if (h >= 24):
    h %= 24

print(h, m)