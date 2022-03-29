import sys
from collections import Counter

input = sys.stdin.readline

a = input().strip()
b = input().strip()

word_length = len(a)

i = word_length - 1
j = word_length

if not Counter(a) == Counter(b):
    print(-1)
elif not a == b:
    while i >= 0:
        j = a.rfind(b[i], 0, j)
        if j == -1:
            break
        i -= 1
    print(i + 1)
else:
    print(0)
