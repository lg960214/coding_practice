n_dict = dict()

for i in range(10):
    n_dict[str(i)] = i

for i in range(ord("A"), ord("Z")+1):
    alpha = chr(i)
    n_dict[alpha] = i-55

A, B = map(str, input().split())

sum_ = 0

for i in range(0, len(A)):
    sum_ += n_dict[str(A[i])]*(int(B)**(len(A)-1-i))

print(sum_)