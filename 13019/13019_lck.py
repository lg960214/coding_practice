import sys
from collections import Counter

sys.stdin = open("testcase.txt", "r")
input = sys.stdin.readline

a = input().strip()
b = input().strip()

word_length = len(a)

i = word_length - 1
j = word_length

if Counter(a) != Counter(b):
    print(-1)
elif a != b:
    while i >= 0:
        j = a.rfind(b[i], 0, j)
        if j == -1:
            break
        i -= 1
    print(i + 1)
else:
    print(0)
