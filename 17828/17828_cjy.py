import string
import math

def get_value(chars):
    return sum(map(lambda x: alpha2value[x], list(chars)))

def is_valid(length, val):
    low = 'A' * length
    high = 'Z' * length
    if get_value(low) <= val <= get_value(high):
        return True
    return False

alpha2value = {char: i for i, char in enumerate(string.ascii_uppercase, start=1)}
value2alpha = {v: k for k, v in alpha2value.items()}
N, X = map(int, input().split())
if is_valid(N, X):
    while X < (N - 1) * 26:
        print("A", end='')
        N -= 1
        X -= 1
    print(value2alpha[X - (N - 1) * 26], end='Z'*(N - 1))
else:
    print("!")
