import sys
import string
sys.stdin = open("testcase.txt", "r")
input = sys.stdin.readline

n, x = map(int, input().split())

dictionary = dict(enumerate(string.ascii_uppercase))

if x / n > 26 or x < n:
    print("!")
else:
    x -= n
    a = x // 25
    b = x % 25
    if b:
        answer = "A" * (n - a - 1) + dictionary[b]
    if not b:
        answer = "A" * (n - a)
    answer += "Z" * a
    print(answer)
