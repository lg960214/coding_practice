import sys
from math import sqrt

input = sys.stdin.readline

minimum, maximum = map(int, input().split())

maximum_sqrt = int(sqrt(maximum))

number = set(range(minimum, maximum + 1))
for num in range(2, maximum_sqrt + 1):
    pow_num = pow(num, 2)
    number -= set(range(minimum - minimum % pow_num, maximum + 1, pow_num))
print(len(number))
