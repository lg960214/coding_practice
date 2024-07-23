dict_ = {'A+' : 4.5,
         'A0' : 4.0,
         'B+' : 3.5,
         'B0' : 3.0,
         'C+' : 2.5,
         'C0' : 2.0,
         'D+' : 1.5,
         'D0' : 1.0,
         'F' : 0.0}

N = 20

sum_ = 0

hg = 0

for i in range(N):
    temp_list = list(map(str, input().split()))

    if (temp_list[2] == 'P'):
        continue
    sum_ += float(temp_list[1]) * dict_[temp_list[2]]
    hg += float(temp_list[1])

print(sum_/hg)