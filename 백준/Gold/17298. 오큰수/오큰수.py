N = int(input())

arr = list(map(int, input().split()))

stk = []
nge = []

for i in range(len(arr)-1, -1, -1):
    # 1. stack에 있는 값이 작거나 같을 경우
    # --> stack이 빌 때까지 탐색
    # --> 없으면 본인을 push하고 -1 넣기
    # 2. stack에 있는 값이 클 경우
    # --> 오큰수 등록 후 본인도 stack에 push
    while (stk):
        if (arr[i] >= stk[-1]):
            stk.pop()
        else:
            nge.append(stk[-1])
            stk.append(arr[i])
            break
    if not (stk):
        stk.append(arr[i])
        nge.append(-1)



for i in range(len(nge)-1, -1, -1):
    print(nge[i], end=' ')
