"""
@ 문제 분석
 [1] 문제 조건
   - R 연산, C 연산 확인 필요

   - 수의 개수 오름차순, 수 오름차순

   출력 전략
     - 0초에서 [r,c] 값 확인
     - t 초에서 [r,c] 값 확인
     - 100초 이후 [r,c] 값 확인

@ 설계
 1. 문제 R연산, C연산 파악
   - DAT 활용
     DAT idx는 101을 넘지 않음
     그러나 쫄리니 1000으로 ㄱㄱ

 2. 연산 진행

 3. 계산된 리스트 값을 arr에 업데이트
   + max row, max col 값 갱신



"""
from heapq import heappush, heappop

def R_operation():
    global My

    for i in range(Mx):
        DAT = [0] * 200
        heap = []
        for j in range(My):
            DAT[arr[i][j]] += 1

        for j in range(1, 200):
            if DAT[j] == 0: continue
            heappush(heap, (DAT[j], j))

        idx = 0

        for j in range(100):
            arr[i][j] = 0

        while heap:
            target = heappop(heap)

            arr[i][idx] = target[1]
            arr[i][idx+1] = target[0]
            idx += 2

            if idx >= 100:
                break

            My = max(My, idx)

def C_operation():
    global Mx

    for j in range(My):
        DAT = [0] * 200
        heap = []
        for i in range(Mx):
            DAT[arr[i][j]] += 1

        for i in range(1, 200):
            if DAT[i] == 0: continue
            heappush(heap, (DAT[i], i))

        for i in range(100):
            arr[i][j] = 0

        idx = 0
        while heap:
            target = heappop(heap)

            arr[idx][j] = target[1]
            arr[idx+1][j] = target[0]
            idx += 2

            if idx >= 100:
                break

            Mx = max(Mx, idx)


arr = [[0]*100 for _ in range(100)]

R, C, K = map(lambda x: int(x)-1, input().split())
K += 1

Mx, My = 3, 3

for i in range(3):
    tmp = list(map(int, input().split()))
    for j, el in enumerate(tmp):
        arr[i][j] = el

if arr[R][C] == K:
    print(0)
else:
    for t in range(100):
        # 1. R & C 연산 파악
        if Mx >= My:
            R_operation()
        else:
            C_operation()

        if arr[R][C] == K:
            print(t+1)
            break
    else:
        print(-1)