import sys
from collections import deque

#sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
input = iter(open(0).read().split('\n')).__next__

class Sol:
    def __init__(self) -> None:
        # 1. Initiation
        direction = []
        DIM = 11
        tomato_0_cnt = 0
        arr = []
        
        for i in range(DIM):
            tmp_lst = [0]*(2*DIM)
            tmp_lst[2*i], tmp_lst[2*i+1] = -1, 1
            direction.append(tmp_lst)
        
        # 2. Input
        mul_q = deque()
        
        DIM_input = list(map(int, input().split())) # m, n, o, p, q, r, s, t, u, v, w
        for w in range(DIM_input[DIM-1]):
            tmp_w = []
            for v in range(DIM_input[DIM-2]):
                tmp_v = []
                for u in range(DIM_input[DIM-3]):
                    tmp_u = []
                    for t in range(DIM_input[DIM-4]):
                        tmp_t = []
                        for s in range(DIM_input[DIM-5]):
                            tmp_s = []
                            for r in range(DIM_input[DIM-6]):
                                tmp_r = []
                                for q in range(DIM_input[DIM-7]):
                                    tmp_q = []
                                    for p in range(DIM_input[DIM-8]):
                                        tmp_p = []
                                        for o in range(DIM_input[DIM-9]):
                                            tmp_o = []
                                            for n in range(DIM_input[DIM-10]):
                                                tmp_n = list(map(int, input().split()))
                                                for m in range(DIM_input[DIM-11]):
                                                    if (tmp_n[m] == 1):
                                                        mul_q.append([w,v,u,t,s,r,q,p,o,n,m])
                                                    elif (tmp_n[m] == 0):
                                                        tomato_0_cnt += 1
                                                tmp_o.append(tmp_n)
                                            tmp_p.append(tmp_o)
                                        tmp_q.append(tmp_p)
                                    tmp_r.append(tmp_q)
                                tmp_s.append(tmp_r)
                            tmp_t.append(tmp_s)
                        tmp_u.append(tmp_t)
                    tmp_v.append(tmp_u)
                tmp_w.append(tmp_v)
            arr.append(tmp_w)
        
        step = 0
        curSize = 0
        
        while mul_q:
            curSize = mul_q.__len__()
            
            for c in range(curSize):
                target = mul_q.popleft()
                
                for i in range(DIM*2):
                    next = []
                    flag = True
                    for j in range(DIM):
                        tmp_next = target[j] + direction[j][i]
                        if not (0 <= tmp_next < DIM_input[DIM-j-1]): 
                            flag = False
                            break
                        next.append(tmp_next)
                        
                    if (flag == False): continue
                    
                    # 2. Array tomato 체크 (0인 것들)
                    element = arr
                    for idx in next[:-1]:
                        element = element[idx]

                    if (element[next[-1]] != 0): continue
                    
                    # 3. array 변경 및 queue 등록
                    element[next[-1]] = 1
                    
                    tomato_0_cnt -= 1
                    mul_q.append(next)
                    
            step += 1
        
        if tomato_0_cnt > 0:
            print(-1)
        else:
            print(step-1)
            
user = Sol()