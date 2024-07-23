from collections import defaultdict

dict_ = dict()

target = input()

for apb in target:
    apb = apb.upper()
    if (dict_.get(apb)):
        dict_[apb] += 1
    else:
        dict_[apb] = 1

flag = False
max_ = 0
max_apb = ''

for item, val in dict_.items():
    if (max_ < val):
        max_apb = item
        max_ = val
        flag = False
    elif (max_ == val):
        flag = True

if (flag):
    print('?')
else:
    print(max_apb)