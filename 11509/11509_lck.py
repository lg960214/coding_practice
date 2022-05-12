import sys
sys.stdin = open('testcase.txt', 'r')
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().strip().split()))

check = [0] * (max(data) + 1)
answer = 0
for num in data:
    if not check[num]:
        answer += 1
        check[num - 1] += 1
    else:
        check[num] -= 1
        check[num - 1] += 1
    
print(answer)
