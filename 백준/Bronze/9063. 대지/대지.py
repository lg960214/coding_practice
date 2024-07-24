N = int(input())

mx = -1e9
my = -1e9
ix = 1e9
iy = 1e9

for _ in range(N):
    a, b = map(int, input().split())
    mx = max(mx, a)
    ix = min(ix, a)
    my = max(my, b)
    iy = min(iy, b)

print((mx-ix)*(my-iy))