import math
a,b = tuple(map(int, input().split()))
# a,b 순서 정렬
if b < a:
    a, b = b, a
# 몇 번째 층인지 계산
def check_level(x):
    level = math.sqrt(x)
    int_level = int(level)
    if level == int_level:
        return int_level
    else:
        return int_level + 1    
level_a = check_level(a)
level_b = check_level(b)
# 층 차이 계산 (x2)
answer = 2 * (level_b - level_a)
# 층과 해당 숫자의 짝,홀이 같은지 여부에 따라 +- 1
if level_a % 2 == a % 2:
    answer -= 1    
if level_b % 2 == b %2:
    answer += 1
print(answer)

