# @ 문제 분석
#
# 1. 문제 조건
# - 정해진 총액 이하에서, 가능한 한 "최대의 총 예산"을 배정하는 것
# --> right 범위와 answer가 어떤 것이 나와야 하는 지 명확하게 보이니 쉬운 이진 탐색 문제
#
# 그렇다면, 최대의 총 예산을 어떻게 구해야 할까?
# --> "주어진 예산요청에서 제일 큰 예산"이 "정수 상한액"이 될 때가 최대이므로, right 값이다.
# --> 무턱대고 right를 1e9를 잡아버리면, 항상 예산을 채우는 경우가 있어 정수 상한선이 1e9가 되어버린다.
#



def PS(expected_budget):
    total = 0
    for needs in budget_lst:
        # 특정한 정수 상한액을 계산하라는 문제 조건
        total += min(needs, expected_budget)

    if (total <= max_budget):
        return True
    return False

N = int(input())

# 이진 탐색에 budget_lst를 활용하는 것이 아니기에, 정렬하지 않아도 됨
budget_lst = list(map(int, input().split()))
max_budget = int(input())

left = 0
right = max(budget_lst) # 주어진 예산 이하로 정수 상한액을 잡아야 한다

ans = -1
while left <= right:
    mid = (left + right) // 2 # 특수한 정수 상한액

    if PS(mid): # 예산을 넘지 않았을 때
        left = mid + 1
        ans = mid
    else:
        right = mid - 1

print(ans)