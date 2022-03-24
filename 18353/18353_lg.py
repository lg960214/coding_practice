import sys

sys.stdin = open('testcase.txt', 'r')
input = sys.stdin.readline

class Sol:

    def __init__(self):
        self.N = int(input())
        self.ability = list(map(int, input().split()))
        
        self.dp = [0]*(self.N)
        self.dp[0] = 1

        self.DP()
        
        print(self.N - max(self.dp))

    def DP(self):
        self.ability.reverse()

        for i in range(1, self.N):
            guide = self.ability[i]
            max_ = 0

            for j in range(i):
                if self.ability[j] < guide:
                    if self.dp[j] > max_:
                        max_ = self.dp[j]
            
            self.dp[i] = max_ + 1


        


if __name__ == '__main__':
    user = Sol()
