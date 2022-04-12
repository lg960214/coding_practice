W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

if x2 >= (W - f):
    x3 = W - f
else:
    x3 = x2

if W - f == 0:
    b1 = 0
else:
    if x1 > W - f:
        b1 = int(H / (c + 1)) * (W - f)
    else:
        b1 = int(H / (c + 1)) * (W - f) - (x3 - x1) * (y2 - y1)

if x2 >= f:
    x3 = f
else:
    x3 = x2

if f == 0:
    b2 = 0
else:
    if x1 > f:
        b2 = int(H / (c + 1)) * f
    else:
        b2 = int(H / (c + 1)) * f - (x3 - x1) * (y2 - y1)
print((b1 + b2) * (c + 1))
