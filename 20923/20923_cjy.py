import sys
from collections import deque

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.ground = deque()
        self.ground_top = 0
    
    def can_push(self):
        if len(self.deck) > 1:
            return 1
        else:
            return 0
        
    def push(self):
        self.ground_top = self.deck.popleft()
        self.ground.append(self.ground_top)
    
    def can_pull(self, against_ground_top):
        if self.name == 'do':
            if self.ground_top == 5 or against_ground_top == 5:
                return 1
        elif self.name == 'su':
            if self.ground_top and against_ground_top and self.ground_top + against_ground_top == 5:
                return 1

    def pull(self, deck):
        self.deck.extend(deck)
    
    def flush_ground(self):
        self.ground.clear()
        self.ground_top = 0

input = sys.stdin.readline

N, M = map(int, input().split())

dodo_deck, suyeon_deck = deque(), deque()

for n in range(N):
    a, b = map(int, input().split())
    dodo_deck.appendleft(a)
    suyeon_deck.appendleft(b)

dodo, suyeon = Player('do', dodo_deck), Player('su', suyeon_deck)

for i in range(M):
    if i % 2 == 0: # dodo turn
        # print('dodo turn')
        if dodo.can_push():
            dodo.push()
        else:
            print(suyeon.name)
            break
    else:
        # print('suyeon turn')
        if suyeon.can_push():
            suyeon.push()
        else:
            print(dodo.name)
            break
    # print('check dodo ring')
    if dodo.can_pull(suyeon.ground_top):
        # print('dodo can ring!')
        dodo.pull(suyeon.ground)
        suyeon.flush_ground()
        dodo.pull(dodo.ground)
        dodo.flush_ground()
        
    # print('check suyeon ring')
    if suyeon.can_pull(dodo.ground_top):
        # print('suyeon can ring!')
        suyeon.pull(dodo.ground)
        dodo.flush_ground()
        suyeon.pull(suyeon.ground)
        suyeon.flush_ground()
else:
    if len(dodo.deck) > len(suyeon.deck):
        print(dodo.name)
    elif len(dodo.deck) < len(suyeon.deck):
        print(suyeon.name)
    else:
        print(dodo.name + suyeon.name)
