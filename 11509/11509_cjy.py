N = int(input())
arrow = [0] * 1000001
result = 0
for height in map(int, input().split()):
    if not arrow[height]:
        result += 1
        arrow[height - 1] += 1
    else:
        arrow[height] -= 1
        arrow[height - 1] += 1
print(result)
