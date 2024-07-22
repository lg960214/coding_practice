target_val = int(input())
N = int(input())

sum_ = 0

for _ in range(N):
    temp1, temp2 = map(int, input().split())
    sum_ += temp1*temp2

if (target_val == sum_):
    print("Yes")
else:
    print("No")
    
    
    
    