# k개를 선택해서 만드는 정수가 중복될 수 있으므로, 중복 제거는 set()을 활용
# Permutation 문제이므로, 전체 탐색
# n <= 10, k <= 4 이므로, 최대 경우의 수는 10x9x8x7 = 5040가지

def rec(step, string):
    global visit
    if (step >= K):
        # int가 str보다 처리속도가 빠름
        package_.add(int(string))
        return

    for i in range(N):
        if (visit[i] == True): continue
        visit[i] = True
        rec(step+1, string + arr[i])
        visit[i] = False

N = int(input())
K = int(input())

arr = []
visit = [False]*N
package_ = set()

for _ in range(N):
    temp = input()
    arr.append(temp)

rec(0, '')

print(len(package_))