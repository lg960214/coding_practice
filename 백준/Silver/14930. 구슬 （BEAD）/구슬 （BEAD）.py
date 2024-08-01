class loc:
    def __init__(self, x, v):
        self.x = x
        self.v = v


# 완전 탄성 충돌 -> 운동에너지 보존 및 질량 같음 -> 충돌 시 속도만 교환
# 구슬의 위치는 변하지 않으므로, 그냥 구슬이 일정한 속도로 움직인다고 생각하면 된다
# 최초 순서만 고려

N, t = map(int, input().split())

beads = []
findIndex = []

for i in range(N):
    x, v = map(int, input().split())
    beads.append(x + v*t)

    if (i == 0):
        # 1번째는 오름차순, 2번째도 오름차순 정렬 --> 같은 위치에서 다른 속도 고려
        findIndex.append([x, v, 1])
    else:
        findIndex.append([x, v, 0])

findIndex.sort()
beads.sort()

for i in range(N):
    if (findIndex[i][2] == 1):
        print(beads[i])
        break