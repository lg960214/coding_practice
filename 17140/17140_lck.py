import sys
from collections import Counter

input = sys.stdin.readline

r, c, k = map(int, input().strip().split())
data = [list(map(int, input().strip().split())) for _ in range(3)]

timer = 0
while timer <= 100:
    if len(data) >= r and len(data[0]) >= c:
        if data[r - 1][c - 1] == k:
            print(timer)
            break

    new_list = []

    # R연산
    if len(data) >= len(data[0]):
        max_row = 0
        for row in data:
            r_list = []
            counter = Counter(row)
            counter = sorted(counter.items(), key=lambda x: (x[1], x[0]))
            for item in counter:
                if item[0] == 0:
                    continue
                r_list.extend(list(item))
            max_row = max(max_row, len(r_list))
            r_list.extend((100 - len(r_list)) * [0])
            new_list.append(r_list)

        max_row = min(100, max_row)
        data = list(map(lambda x: x[:max_row], new_list))
    # C연산
    else:
        max_col = 0
        data.extend([0] * len(data[0]) for _ in range(len(data)))
        for i in range(len(data[0])):
            c_list = []
            col = [row[i] for row in data]
            counter = Counter(col)
            counter = sorted(counter.items(), key=lambda x: (x[1], x[0]))
            for item in counter:
                if item[0] == 0:
                    continue
                c_list.extend(list(item))
            max_col = max(max_col, len(c_list))
            c_list.extend((len(data) - len(c_list)) * [0])
            for idx, item in enumerate(c_list):
                data[idx][i] = item
        max_col = min(100, max_col)
        data = data[:max_col]

    timer += 1
else:
    print(-1)
