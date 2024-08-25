# @ 연결리스트를 이용한 풀이
import time

class Node:
    def __init__(self, durable):
        self.durable = durable # 내구도 정보
        self.next = None # next node pointer
        self.prev = None # previous node pointer
        self.robot = False # robot 여부

    def __str__(self): # 디버깅용 str 선언
        if self.prev != None and self.next != None:
            return f'{self.durable} {self.robot}'
        if self.prev == None and self.next != None:
            return f'{self.durable} {self.robot}'
        if self.prev != None and self.next == None:
            return f'{self.durable} {self.robot}'
        else:
            return f'{self.durable} {self.robot}'

    def __repr__(self):
        return f'{self.durable} {self.next} {self.prev} {self.robot}'

N, K = map(int, input().split())

A = list(map(int, input().split())) # 내구도 정보


first_node = None
last_node = None

for i in range(2*N):
    if i == 0:
        first_node = Node(A[0])
        cur_node = first_node
    else:
        cur_node = Node(A[i])
        past_node.next = cur_node
        cur_node.prev = past_node
        if i == N-1:
            last_node = cur_node
    past_node = cur_node
else:
    past_node.next = first_node
    first_node.prev = past_node

step = 1 # 1단계부터 시작

be_robot_idx = 0 # 컨베이어 위에 있는 로봇 시작 인덱스
robot_lst = [] # 로봇이 들어 있는 노드만 저장하여 따로 관리

while True:

    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    # --> 한 칸 뒤로 pointer 이동
    first_node = first_node.prev
    last_node = last_node.prev

    # 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
    if last_node.robot == True:
        last_node.robot = False
        be_robot_idx += 1

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로
    for i in range(be_robot_idx, len(robot_lst)): # 가장 먼저 벨트에 올라간 로봇부터
        # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며
        current_bot = robot_lst[i]
        next_bot = current_bot.next

        # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며,
        if next_bot.robot == True: continue
        #  그 칸의 내구도가 1 이상 남아 있어야 한다.
        if next_bot.durable <= 0: continue

        # 한 칸 이동할 수 있다면 이동한다.
        current_bot.robot = False
        next_bot.durable -= 1
        if next_bot.durable == 0:
            K -= 1
            next_bot.durable -= 1

        if current_bot.next == last_node: # 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
            be_robot_idx += 1
        else:
            next_bot.robot = True
            robot_lst[i] = next_bot


    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면
    # 올리는 위치에 로봇을 올린다.
    if first_node.durable > 0:
        # 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면
        # 그 칸의 내구도는 즉시 1만큼 감소한다.
        first_node.robot = True
        first_node.durable -= 1
        robot_lst.append(first_node)

        if first_node.durable == 0:
            K -= 1
            first_node.durable -= 1

    tmp = first_node
    if K <= 0:
        break

    step += 1

print(step)