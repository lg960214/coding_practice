"""
@ 문제 분석
  - 표
    - 크기 : 50 × 50 고정
    - 위에서 r번째, 왼쪽에서 c번째 --> 기존 풀이와 똑같이 진행
      - Ri, Ci의 범위는 1 ~ 50으로 주어짐
  - cell
    - 초기값 - 비어 있음
    - 문자열 값을 가짐
    - 다른 cell과 병합 가능
  - commands
    - 총 1,000개 주어짐
    - UPDATE(2), MERGE(1), UNMERGE(1), PRINT(1) 함수가 있음

    - "UPDATE r c value" : cell의 값을 value로 바꿈
      - value : 셀에 입력할 내용

    - "UPDATE value1 value2"
      - value1을 값으로 가지고 있는 모든 셀을 선택
        - 선택한 cell의 값을 value로 바꿈
      - value1 : 선택할 cell의 값
      - value2 : cell에 입력할 내용
      - 소문자 + 숫자로 이루어진 길이가 1~10인 문자열

      ? 같은 값을 가지는 cell이 있을까? --> O
      ! Union-Find 문제인가?

    - "MERGE r1 c1 r2 c2"
      - (r1,c1)과 (r2, c2)를 모두 합친다
      - 같은 cell이면 무시 (merge 포함)
      - 인접하지 않을 수도 있음 (사이는 무시)
      - value 조건
        - 두 셀 중 한 셀만 값을 가지고 있다면 --> 그 값을 가짐
        - 두 셀 모두 값을 가지면 --> r1, c1 위치의 cell 값을 가짐
        - 이후 (r1, c1), (r2, c2) 중 어느 걸 선택해도 병합된 cell로 접근

    - "UNMERGE r c"
      - (r, c) 위치의 셀을 선택하여 해당 셀의 모든 병합을 해제
      - 병합을 해제하기 전 셀이 값을 가지고 있었을 경우
        (r, c) 위치의 셀이 그 값을 가지게 됩니다.
      ? 해당 조건 검증 필요
      --> 아하 값이 있으면 나머지는 empty, 값은 r, c가 갖는다!

    - "PRINT r c"
      - (r, c) 위치의 셀을 선택하여 셀의 값을 출력
      - 선택한 셀이 비어있을 경우 "EMPTY"를 출력


@ 설계 ( ~43)
기본적으로, 문제에서 주어진 array처럼 활용해야 한다

시간복잡도 : 2,500 x 1,000 = 2 500 000 -> 여유

1. index_table과 value_table로 분리해볼까?
  command 길이는 1,000인 걸 고려해보자
  - index_table은 현재 index 값을 넣어주고
  - value_table은 모두 "None" 값으로 시작

  - "UPDATE r c value"
    - index_table에서, 부모로 (r, c) 값을 가지는 애들 모두에게 진행 : 2,500
    - 그냥 value 모두 넣어야 unmerge할 때 편하다

  - "UPDATE value1 value2"
    - value_table에서, value1을 갖는 것들을 value2로 바꿔줌 : 2,500

  - "MERGE r1 c1 r2 c2"
    (r1, c1)과 (r2, c2) 중, row-first order로 부모를 선택
    - value (r1, c1) 우선, None이면 (r2, c2)를 선택
    - index_table에서 자식으로 선택된 idx를 부모로 모두 바꿔줌

  - "UNMERGE r c"
    - (r, c)로 되어 있는 곳의 값을 따로 저장하고,
    - index_table에서 (r,c)가 저장된 값은 모두 None 처리
    - (r, c)에만 저장했던 값 update

  - "PRINT r c"
    - index에 (r, c)로 되어있는 곳 찾아서 출력하고 break

@ 구현


@ 검증
 - TC 1차 검증 완료
"""

def update_1(cur_str, next_str):
    # value_table에서, value1을 갖는 것들을 value2로 바꿔줌
    for i in range(50):
        for j in range(50):
            if value_arr[i][j] == cur_str and index_arr[i][j] == (i, j):
                value_arr[i][j] = next_str

    return

def update_2(x, y, value):
    # index_table에서, 부모로 (r, c) 값을 가지는 애에게 진행
    tx, ty = index_arr[x][y]

    value_arr[tx][ty] = value
    return

def merge(x1, y1, x2, y2):
    # (r1, c1)과 (r2, c2) 중, row major order로 부모를 선택
    # - value (r1, c1) 우선, None이면 (r2, c2)를 선택
    # - index_table에서 자식으로 선택된 idx를 부모로 모두 바꿔줌

    tx1, ty1 = index_arr[x1][y1]
    tx2, ty2 = index_arr[x2][y2]

    value = value_arr[tx1][ty1]
    if value == None:
        value = value_arr[tx2][ty2]

    c1 = 50*tx1 + ty1
    c2 = 50*tx2 + ty2

    if c1 == c2: # 선택한 두 위치의 셀이 같은 셀일 경우 무시합니다.
        return
    elif c2 < c1:
        tx1, tx2 = tx2, tx1
        ty1, ty2 = ty2, ty1


    for i in range(50):
        for j in range(50):
            if index_arr[i][j] == (tx2, ty2):
                index_arr[i][j] = (tx1, ty1)

    value_arr[tx1][ty1] = value
    return

def unmerge(x, y):
    # (r, c)로 되어 있는 곳의 값을 따로 저장하고,
    # index_table에서 (r,c)가 저장된 값은 모두 None 처리
    # (r, c)에만 저장했던 값 update
    tx, ty = index_arr[x][y]
    value = value_arr[tx][ty]

    for i in range(50):
        for j in range(50):
            if index_arr[i][j] == (tx, ty):
                value_arr[i][j] = None
                index_arr[i][j] = (i, j)

    value_arr[x][y] = value
    return

def _print(x, y):
    tx, ty = index_arr[x][y]

    value = value_arr[tx][ty]

    if value == None:
        return "EMPTY"
    return value

index_arr = []
value_arr = []

def solution(commands):
    answer = []

    for i in range(50):
        tmp_idx = []
        tmp_val = []
        for j in range(50):
            tmp_idx.append((i, j))
            tmp_val.append(None)
        index_arr.append(tmp_idx)
        value_arr.append(tmp_val)

    for i in range(len(commands)):
        target = commands[i].split()

        if target[0] == 'UPDATE':
            if len(target) == 3:
                update_1(target[1], target[2])
            elif len(target) == 4:
                update_2(int(target[1])-1, int(target[2])-1, target[3])
        elif target[0] == 'MERGE':
            merge(int(target[1])-1, int(target[2])-1, int(target[3])-1, int(target[4])-1)
        elif target[0] == 'UNMERGE':
            unmerge(int(target[1])-1, int(target[2])-1)
        elif target[0] == 'PRINT':
            answer.append(_print(int(target[1])-1, int(target[2])-1))

    return answer