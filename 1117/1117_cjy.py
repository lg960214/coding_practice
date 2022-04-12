W, H, f, c, x1, y1, x2, y2 = map(int, input().split())
if c:
    y_fold = c + 1
else:
    y_fold = 1

if 0 < f < W:
    f = min(f, W - f)
    x_fold = 2
else:
    x_fold = 1

count = 0
if x1 < x2 <= f:
    n_square = (x2 - x1) * (y2 - y1)
    count += n_square * x_fold * y_fold
elif x1 < f < x2:
    n_square = (f - x1) * (y2 - y1)
    count += n_square * x_fold * y_fold
    n_square = (x2 - f) * (y2 - y1)
    count += n_square * y_fold
else:
    n_square = (x2 - x1) * (y2 - y1)
    count += n_square * y_fold
print(W * H - count)
