N = int(input())

target_list = list(map(int, input().split()))

max_val = max(target_list)

for i in range(len(target_list)):
    target_list[i] = (target_list[i] * 100) / max_val

print(sum(target_list)/len(target_list))