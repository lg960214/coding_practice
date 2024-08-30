"""

@ 문제 분석
  [1] 문제 조건
  - NxN 교실, 학생 수도 N^2 (번호가 따로 매겨져 있음)
  - 범위는 1 ~ N

  [2] 시간 복잡도 (N=20)

  1. 8방향 x 좋아하는 사람 체크 x N^2 = 3200
  2. 빈 칸 체크 = 3200
  3. sort() = N^2logN^2 = 약 4000
  4. 만족도 = N^2 x 8방향 = 3200

  그냥 구현해도 시간 복잡도 초과는 나지 않을듯 하다

  [3] 나머지 조건 체크
  - 특이사항 없음

@ 설계
  [0] input : 범위 0 ~ N-1로 받음
   - 좋아하는 애들은 set이나 list나 별 차이 없어서 list로 진행

  나머지는 시뮬레이션이라, 진행하면서 해도 무방할듯
  [1]
  단, [2] 과정에서 값을 저장

@ 검증
  array 까보다가 indentation 오류 찾음

"""

def test_1(s):
    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    max_ = 0
    candidate = []

    like_people = student_lst[s]

    for i in range(N):
        for j in range(N):
            if arr[i][j] != -1: continue

            like_cnt = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 > nx or 0 > ny or N <= nx or N <= ny: continue
                if arr[nx][ny] in like_people:
                    like_cnt += 1

            if max_ < like_cnt:
                max_ = like_cnt
                candidate = [(i, j)]
            elif max_ == like_cnt:
                candidate.append((i, j))

    return candidate

def test_2(student, prev_c_loc):

    max_ = 0
    candidate = []

    for i, loc in enumerate(prev_c_loc):
        empty_cnt = 0
        for d in range(4):
            nx = loc[0] + dx[d]
            ny = loc[1] + dy[d]
            if 0 > nx or 0 > ny or N <= nx or N <= ny: continue

            if arr[nx][ny] == -1:
                empty_cnt += 1

        if max_ < empty_cnt:
            max_ = empty_cnt
            candidate = [loc]
        elif max_ == empty_cnt:
            candidate.append(loc)

    return candidate

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())

arr = [[-1]*N for _ in range(N)] # 0번도 학생이니까

student_lst = [[] for _ in range(N**2)]
student_order = []
for _ in range(N**2):
    s_id, *s_like = list(map(lambda x: int(x)-1, input().split()))
    student_lst[s_id] = s_like
    student_order.append(s_id)

for student in student_order:
    # 1. 빈 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정함
    canBe = test_1(student)
    if len(canBe) == 1:
        arr[canBe[0][0]][canBe[0][1]] = student
        continue

    # 2. 1을 만족하는 칸이 여러 개이면,
    #    인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    canBe = test_2(student, canBe)

    if len(canBe) == 1:
        arr[canBe[0][0]][canBe[0][1]] = student
        continue

    # 3. 2을 만족하는 칸이 여러 개이면, row first order로 정함
    canBe.sort()
    arr[canBe[0][0]][canBe[0][1]] = student

good_score = [0, 1, 10, 100, 1000]
total_good = 0

for i in range(N):
    for j in range(N):
        good_cnt = 0
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 > nx or 0 > ny or N <= nx or N <= ny: continue
            if arr[nx][ny] in student_lst[arr[i][j]]:
                good_cnt += 1
        total_good += good_score[good_cnt]

print(total_good)