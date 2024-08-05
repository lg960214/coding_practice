N, L, R, X = list(map(int, input().split()))

Ai = list(map(int, input().split()))

# Bit Operations

# 1. 1 <= N <= 15이므로, 2**15 가지의 경우를 bitmasking으로 검증

answer = 0

thr = 1<<N
bm = 1
while (bm < thr):
    level_sum = 0
    max_level, min_level = -1, 21e9

    for i in range(N):
        flag = bm & (1<<i)

        # 선택된 문제
        if (flag):
            # 1. 최고 난이도, 최저 난이도 구하기
            max_level = max(Ai[i], max_level)
            min_level = min(Ai[i], min_level)
            # 2. 난이도의 합 구하기
            level_sum += Ai[i]

    # 3. 최고 난이도, 최저 난이도 차 계산
    if (max_level - min_level >= X) and (L <= level_sum <= R):
        answer += 1

    bm += 1


print(answer)