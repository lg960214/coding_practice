n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
stk = []
idx = 0
result = []
for i in range(1, n+1):
    stk.append(i)
    result.append('+')
    while stk and (nums[idx] == stk[-1]):
        stk.pop()
        result.append('-')
        idx += 1

if not stk:
    for i in range(len(result)):
        print(result[i])
else:
    result = 'NO'
    print(result)
