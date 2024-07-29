K = int(input())

stack_ = []

for _ in range(K):
    temp = int(input())
    if (temp == 0):
        stack_.pop()
    else:
        stack_.append(temp)
        
print(sum(stack_))