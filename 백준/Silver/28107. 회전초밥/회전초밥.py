# IndexError 원인 추측 : 주방장이 만든 초밥(Ai)이 200,000일 수도 있으므로
# --> food_lst의 index를 늘려준다
#
# @ 문제 분석
#
# (1) 문제 조건
# 1. 요리사는 M개의 초밥을 순서대로 만든다
# --> 1번부터 N번까지의 손님의 순서대로 초밥을 받는다
# --> 앞 사람이 원하는게 나오면, 먼저 먹는다
#
# 2. (목록 순서에 상관 없이) 목록에 적힌 초밥이 앞에 오면 반드시 먹는다
# --> 초밥은 최대 한 번만 먹는다
#
# 위의 내용으로 말미암아 볼 때, 예제로 시뮬레이션을 돌려 보면
# 요리사가 3을 만든다 --> 3이 필요한 사람 --> 2번 손님이 먹는다
# 요리사가 2를 만든다 --> 2가 필요한 사람 --> 2번 손님이 먹는다
# 요리사가 1을 만든다 --> 1이 필요한 사람 --> 1번 손님이 먹는다
# ...
# 이런 식으로 흘러갈 것이다
#
# 음식이 필요한 사람을 빠르게 찾아내려면,
# 해당 음식을 index로 하는 array를 만들고, 거기에 heapq로 대기 손님을 넣어야 할 것이다
#
# 예시 1로 heapq로 만들어 보려면,
# [None, heapq{1, 3), heapq(2), heapq(2), heapq(), heapq(2), heapq(1)]
# 가 될 것이다
#
# (2) 시간복잡도
# A. 초밥 개수(K)가 200,000개 이하이고 heapify 시간복잡도는 logK
# --> logK
# B. 요리되는 초밥은 M번 꺼내야 한다
# --> M
# 따라서 시간복잡도는 M*logK가 될 것 같다


import sys, heapq

input = sys.stdin.readline

N, M = map(int, input().split())

food_lst = [[] for _ in range(200001)] # 초밥 인덱스 : Ai는 200,000 이하

for i in range(1, N+1):
    order_lst = list(map(int, input().split()))[1:] # i번째 손님의 주문 사항

    for food in order_lst:
        heapq.heappush(food_lst[food], i) # i번째 손님이 food list index에 추가됨

make_order = list(map(int, input().split())) # 주방장이 스시를 만든다

answer_lst = [0]*(N+1) # 손님이 먹은 초밥 개수를 세는 칸

for sushi in make_order:
    if food_lst[sushi]: # 만든 스시를 기다리는 사람이 있다면
        answer_lst[heapq.heappop(food_lst[sushi])] += 1 # 가장 index가 작은 손님이 초밥을 먹는다

print(*answer_lst[1:])




