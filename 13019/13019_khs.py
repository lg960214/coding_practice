A = str(input())
B = str(input())
a_len = len(A)
import collections
A_dict = collections.defaultdict(int)
B_dict = collections.defaultdict(int)
for i in range(a_len):
    A_dict[A[i]] += 1
    B_dict[B[i]] += 1
if not A_dict == B_dict:
    print(-1)
else:
    last_ind = a_len -1
    for i in range(a_len -1,-1,-1):
        a = A[i]
        b = B[i]
        if a == b:
            continue
        else:
            last_ind = i
            break
            
    A = A[:last_ind + 1]
    B = B[:last_ind + 1]  
    a_len = len(A)
    
    ind = -1
    base = B[ind]
    answer = 0

    for i in range(a_len -1,-1,-1):
        a = A[i]
        if a == base:
            ind -= 1
            if ind * -1 >= a_len:
                break
            base = B[ind]
        else:
            answer += 1
    print(answer)

