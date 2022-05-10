n = int(input())
h = list(map(int, input().split()))

answer = 0
h_list = [0]*1000001

for i in h:
    if h_list[i] == 0:
        h_list[i-1] += 1
        answer += 1
    else:
        h_list[i] -= 1
        h_list[i-1] += 1

print(answer)

