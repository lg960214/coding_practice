# @ 문제 분석
#
# [1] 문제 조건
# 표의 위 선택, 아래 선택, 삭제, 복구 함수 구현하는 것
#
# 1. 위 선택
#   - 현재 선택된 행에서 X칸 위에 있는 행을 선택
# 2. 아래 선택
#   - 현재 선택된 행에서 X칸 아래에 있는 행을 선택
# 3. 삭제
#   - 현재 행 삭제 후, 바로 아래 행 선택
#   - 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택
# 4. 복구
#   - 가장 최근에 삭제된 행을 원래대로 복구
#   - 단, 현재 선택된 행은 바뀌지 않습니다

# [2] 시간복잡도
# n = 1,000,000 (행 수)
# cmd 원소 개수 : 200,000
# 명령 200,000번이 들어온다.
# --> 모든 X들의 값을 합친 결과가 1,000,000 이하인 경우만 입력으로 주어집니다
# 이동은 1,000,000번 이하란 소리
# -> Up 함수와 Down 함수는 최대 1,000,000 번 연산을 할 수 있다 (X 값 제외) --> O(N)으로 구현
# -> Add와 Remove 함수는 O(1)로 구현해야 함

# @ 설계
# 1. Up 함수
# - O의 개수만을 세서 올라감 (표의 범위를 벗어나는 이동은 입력으로 주어지지 않습니다.)
# - 연결리스트 활용

# 2. Down 함수
# - O의 개수만을 세서 내려감 (표의 범위를 벗어나는 이동은 입력으로 주어지지 않습니다.)
# - 연결리스트 활용

# 3. Remove 함수
# - prev Node와 next Node 정보를 연결해주는 함수

# 4. Add 함수
# - 저장되어 있는 current Node를 기존의 prev와 next를 연결해준다
# - 순차적으로 빼서 연결하기 때문에, 오류는 발생하지 않음

class Node:
    def __init__(self, idx):
        self.idx = idx  # cursor 변경용
        self.be = 'O'  # OX 표시용
        self.prev = None
        self.next = None
    
    def __repr__(self):
        return f'{self.be}'


arr = []
remove_lst = []


def U(loc, rep):  # 커서 올림
    target = arr[loc]

    for _ in range(rep): # 표의 범위를 벗어나는 이동은 입력으로 주어지지 않습니다.
        target = target.prev

    return target.idx


def D(loc, rep):  # 커서 내림
    target = arr[loc]

    for _ in range(rep): # 표의 범위를 벗어나는 이동은 입력으로 주어지지 않습니다.
        target = target.next

    return target.idx


def C(loc):  # 제거 : 원래대로 복구할 행이 없을 때(즉, 삭제된 행이 없을 때) "Z"가 명령어로 주어지는 경우는 없습니다.
    targetNode = arr[loc]
    remove_lst.append(targetNode)
    targetNode.be = 'X'
    
    if targetNode.prev != None:    
        targetNode.prev.next = targetNode.next
    if targetNode.next != None:
        targetNode.next.prev = targetNode.prev

    
    if targetNode.next == None: # 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
        return targetNode.prev.idx
    else: # 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다.
        return targetNode.next.idx


def Z():  # 가장 최근에 삭제된 행을 원래대로 복구
    targetNode = remove_lst.pop()
    targetNode.be = 'O'
    
    if targetNode.prev != None:
        targetNode.prev.next = targetNode
    if targetNode.next != None:
        targetNode.next.prev = targetNode

    return # 단, 현재 선택된 행은 바뀌지 않습니다


def solution(n, k, commands):
    arr.append(Node(0))

    prev = arr[0]

    for i in range(1, n):
        cur = Node(i)

        cur.prev = prev
        prev.next = cur

        arr.append(cur)

        prev = cur

    cursor = k

    for cmd in commands:
        p_cmd = cmd.split()

        if p_cmd[0] == 'U':  # 커서 올리기
            cursor = U(cursor, int(p_cmd[1]))
        elif p_cmd[0] == 'D':  # 커서 내리기
            cursor = D(cursor, int(p_cmd[1]))
        elif p_cmd[0] == 'C':  # 커서 제거
            cursor = C(cursor)
        elif p_cmd[0] == 'Z':  # 커서 복구
            Z()
        
    ans = ''

    for node in arr:
        ans += node.be

    return ans