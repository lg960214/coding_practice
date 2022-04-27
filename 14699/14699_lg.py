import sys
from copy import deepcopy

sys.stdin = open('testcase.txt','r')
input = sys.stdin.readline


class Sol:

    def __init__(self):
        N, M = map(int, input().split())
        height = list(map(int, input().split()))
        dp = [1]*(N)
        node = [[0]*(N) for i in range(N)]
        
        for _ in range(M):
            x, y = map(int, input().split())
            node[x-1][y-1] = 1
            node[y-1][x-1] = 1
        
        height_sort = deepcopy(height)
        height_sort.sort(reverse=True)

        height_idx = []
        
        for factor in height_sort:
            idx = height.index(factor)
            height_idx.append(idx)

        
        for h in height_idx:
            for i in range(N):
                if (height[h] < height[i]) and (node[h][i] == 1):
                    dp[h] = max(dp[h], dp[i]+1)

        for i in dp:
            print(i)


if __name__ == '__main__':
    user = Sol()