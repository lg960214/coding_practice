N, M = map(int, input().split())

arr = [input() for _ in range(N)]

# 흰색 체스판
W_ex = ["WBWBWBWB", "BWBWBWBW",
     "WBWBWBWB", "BWBWBWBW",
     "WBWBWBWB", "BWBWBWBW",
     "WBWBWBWB", "BWBWBWBW"]

# 검은색 체스판
B_ex = ["BWBWBWBW", "WBWBWBWB",
        "BWBWBWBW", "WBWBWBWB",
        "BWBWBWBW", "WBWBWBWB",
        "BWBWBWBW", "WBWBWBWB"]

min_ = 1e9
for i in range(N-7):
    for j in range(M-7):
        W_cnt = 0
        B_cnt = 0
        for a in range(8):
            for b in range(8):
                if (arr[i+a][j+b] == W_ex[a][b]):
                    W_cnt += 1
                if (arr[i+a][j+b] == B_ex[a][b]):
                    B_cnt += 1
        min_ = min(min(W_cnt, B_cnt), min_)

print(min_)