import sys

sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline


class Sol:
    def __init__(self):
        temp = list(map(int, input().split()))

        self.behind = [temp[:2], temp[2:4]]
        self.down = [temp[4:6], temp[6:8]]
        self.front = [temp[8:10], temp[10:12]]
        self.left = [temp[12:14], temp[14:16]]
        self.right = [temp[16:18], temp[18:20]]
        self.top = [temp[20:22], temp[22:24]]

        for i in range(1, 7):
            sum_ = self.roll(i)
            if sum_ == 6:
                print(1)
                break
        else:
            print(0)

    def roll(self, method):
        # R'1
        if method == 1:
            a = set([self.behind[0][0], self.behind[1][0], self.down[0][1], self.down[1][1]])
            b = set([self.down[0][0], self.down[1][0], self.front[0][1], self.front[1][1]])
            c = set([self.front[0][0], self.front[1][0], self.top[0][0], self.top[1][0]])
            d = set([self.top[0][1], self.top[1][1], self.behind[0][1], self.behind[1][1]])
            e = set(self.left[0] + self.left[1])
            f = set(self.right[0] + self.right[1])
        # R1
        elif method == 2:
            a = set([self.behind[0][0], self.behind[1][0], self.top[0][0], self.top[1][0]])
            b = set([self.top[0][1], self.top[1][1], self.front[0][1], self.front[1][1]])
            c = set([self.front[0][0], self.front[1][0], self.down[0][1], self.down[1][1]])
            d = set([self.down[0][0], self.down[1][0], self.behind[0][1], self.behind[1][1]])
            e = set(self.left[0] + self.left[1])
            f = set(self.right[0] + self.right[1])
        # F1
        elif method == 3:
            a = set([self.down[1][0], self.down[1][1], self.left[0][0], self.left[0][1]])
            b = set([self.right[1][0], self.right[1][1], self.down[0][0], self.down[0][1]])
            c = set([self.top[1][0], self.top[1][1], self.right[0][0], self.right[0][1]])
            d = set([self.left[1][0], self.left[1][1], self.top[0][0], self.top[0][1]])
            e = set(self.front[0] + self.front[1])
            f = set(self.behind[0] + self.behind[1])
        # F'1
        elif method == 4:
            a = set([self.down[1][0], self.down[1][1], self.right[0][0], self.right[0][1]])
            b = set([self.right[1][0], self.right[1][1], self.top[0][0], self.top[0][1]])
            c = set([self.top[1][0], self.top[1][1], self.left[0][0], self.left[0][1]])
            d = set([self.left[1][0], self.left[1][1], self.down[0][0], self.down[0][1]])
            e = set(self.front[0] + self.front[1])
            f = set(self.behind[0] + self.behind[1])
        # U'1
        elif method == 5:
            a = set([self.behind[0][0], self.behind[0][1], self.left[0][1], self.left[1][1]])
            b = set([self.left[0][0], self.left[1][0], self.front[0][0], self.front[0][1]])
            c = set([self.front[1][0], self.front[1][1], self.right[0][0], self.right[1][0]])
            d = set([self.right[0][1], self.right[1][1], self.behind[1][0], self.behind[1][1]])
            e = set(self.top[0] + self.top[1])
            f = set(self.down[0] + self.down[1])
        # U1
        elif method == 6:
            a = set([self.behind[0][0], self.behind[0][1], self.right[0][0], self.right[1][0]])
            b = set([self.right[0][1], self.right[1][1], self.front[0][0], self.front[0][1]])
            c = set([self.front[1][0], self.front[1][1], self.left[0][1], self.left[1][1]])
            d = set([self.left[0][0], self.left[1][0], self.behind[1][0], self.behind[1][1]])

            e = set(self.top[0] + self.top[1])
            f = set(self.down[0] + self.down[1])

        return len(a)+len(b)+len(c)+len(d)+len(e)+len(f)



            






if __name__ == '__main__':
    user = Sol()