import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    if N == 1:
        print(1)
        continue
    
    p_info = dict()
    i_info = dict()
    candidates = set()
    for n in range(N):
        p_info[n], i_info[n] = map(int, input().split())
        candidates.add(n)

    p_ranker_list = list(map(lambda x: x[0], sorted(p_info.items(), key=lambda x: x[1])))
    cutline = i_info[p_ranker_list[0]]
    for candidate in p_ranker_list:
        i_rank_candidate = i_info[candidate]
        if i_rank_candidate > cutline:
            candidates.discard(candidate)
        else:
            cutline = i_rank_candidate
    print(len(candidates))
