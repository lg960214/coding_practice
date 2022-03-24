import sys

sys.stdin = open("testcase.txt", "r")
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
m = int(input())


def binary_search():
    left = 0
    right = max(data)
    answer = 0
    while left <= right:
        center = (left + right) // 2
        total = 0
        for budget in data:
            if budget < center:
                total += budget
            else:
                total += center
        if total > m:
            right = center - 1
        elif total <= m:
            answer = center
            left = center + 1
    return answer


if sum(data) <= m:
    print(max(data))
else:
    print(binary_search())
