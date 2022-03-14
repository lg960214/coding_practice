#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import itertools
days,minus = tuple(map(int, input().split()))
kit = list(map(int, input().split()))
total = 500
kit_perm = list(itertools.permutations(kit))
answer = len(kit_perm)

for one_kit in kit_perm:
    total_ = total
    for weight in one_kit:
        total_ += weight
        total_ -= minus
        if total_ < 500 :
            answer -= 1
            break
print(answer)    

