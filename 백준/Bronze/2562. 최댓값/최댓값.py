N = 9

list_ = []

for i in range(N):
    temp = int(input())
    list_.append(temp)
    
    
max_ = 0
max_idx = 0

for i in range(N):
    if (max_ < list_[i]):
        max_ = list_[i]
        max_idx = i

print(max_)
print(max_idx+1)