# @ 문제 분석
# 1. 문제 조건
# - 연산자 우선 순위를 무시하고, 앞에서부터 진행한다
# - 음수를 양수로 나눌 때는, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다
#
# 2. 시간복잡도
# - 최악의 경우, N=11이고 연산자 4개가 3,3,2,2로 주어졌을 경우이므로
# - 계산해야 하는 경우의 수는 10P10 / 3!*3!*2!*2! = 25,200
# - operator 연산까지 고려해도 시간초과는 나지 않는다
# - 가지치기를 하기엔 위험성이 있어서 brute force로 접근할 예정

# @ 설계
# 1. 연산자를 배치한다
# - 어떻게 배치할 지는 재귀를 활용하는 것이 제일 쉽다
# 2. 배치한 연산자를 활용해서 계산한다
# - min,max값만 update 잘 해주면 된다
# --> 중간 계산 결과는 항상 -10억 <= x <= 10억 이므로, 이를 고려해서 정한다

# @ 구현
# 아래 내용 참고

# @ 검증
# N = 11일 때 25,200의 경우의 수 나오는 것 확인
# N = 1 : 확인 완료

def calculate():
    global min_, max_
    value = A[0]

    for i in range(N-1):
        value = operator_[operatorForCal[i]](value, A[i+1])

    max_ = max(max_, value)
    min_ = min(min_, value)


def locateOperators(step):
    if (step == N-1): # operator 배치가 끝났다면, 계산을 시작
        calculate()
        return

    for i in range(4):
        if operator_lst[i] == 0: continue
        operator_lst[i] -= 1
        operatorForCal.append(i)
        locateOperators(step + 1)
        operatorForCal.pop()
        operator_lst[i] += 1

# 1. 함수 정의
# 문제 조건에 따라 함수를 정의하고 활용한다
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if a*b > 0:
        return abs(a)//abs(b)
    else:
        return -(abs(a)//abs(b))

operator_ = [add, sub, mul, div]

N = int(input())
A = list(map(int, input().split()))
operator_lst = list(map(int, input().split()))

operatorForCal = []
min_, max_ = 2e9, -2e9 # 문제 조건에서의 최대/최소를 삽입 --> [-10억, 10억]

locateOperators(0) # 계산 전 operator를 배치하는 함수

print(max_)
print(min_)