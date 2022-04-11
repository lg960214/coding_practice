import sys
from collections import deque


input = sys.stdin.readline


class Sol:
    su_deck = deque()
    do_deck = deque()
    su_ground = deque()
    do_ground = deque()

    def __init__(self):
        self.N, self.M = map(int,input().split())
        
        for _ in range(self.N):
            a, b = map(int,input().split())
            self.do_deck.appendleft(a)
            self.su_deck.appendleft(b)

        player = 0
        do_card = 0
        su_card = 0

        while self.M:
            if player == 0:
                do_card = self.do_deck.popleft()
                self.do_ground.append(do_card)
            else:
                su_card = self.su_deck.popleft()
                self.su_ground.append(su_card)

            if len(self.do_deck) == 0:
                break
            if len(self.su_deck) == 0:
                break

            if (do_card == 5) or (su_card == 5):
                self.do_deck.extend(self.su_ground)
                self.do_deck.extend(self.do_ground)
                self.do_ground = deque()
                self.su_ground = deque()
                do_card = 0
                su_card = 0

            elif (do_card + su_card == 5):
                self.su_deck.extend(self.do_ground)
                self.su_deck.extend(self.su_ground)
                self.do_ground = deque()
                self.su_ground = deque()
                do_card = 0
                su_card = 0

            self.M -= 1

            if player == 0:
                player = 1
            else:
                player = 0


        if len(self.do_deck) > len(self.su_deck):
            print('do')
        elif len(self.do_deck) < len(self.su_deck):
            print('su')
        else:
            print('dosu')






        
if __name__ == '__main__':
    user = Sol()