# @ 문제 분석
# 1. 문제 조건
#  - 전체 N개의 단어
#    - 1 <= N <= 50
#    - 단어의 길이 : 8 <= N <= 15
#    - 중복되는 단어 없음
#
#  - K개의 글자 가르치기
#    - 0 <= K <= 26
#    - 영어 소문자
#
# 2. 인사이트
#  - abcde
#  - fghij
#  - klmno
#  - pqrst
#  - uvwxy
#  - z
#  --> 알파벳이 26개라 제한이 26개
#  --> 순서가 상관없으므로 combination 문제, 
#  
#  - 남극언어의 모든 단어는 "anta"로 시작되고, "tica"로 끝난다. --> 5개 미리 검사
#  --> K < 5 : print(0)
#  - 그럼 a c i n t를 제외하고 진행한다 했을 때, [:4] + [:-4]로 간다
#  - 단어의 길이는 0 <= length <= 7
#  - 알파벳 검사는 21개 (a c i n t가 나오면 중단하는 식으로 backtracking을 구현해야 할듯)
#  - 7 x 50 = 350 번의 검사
#  - 21C10이 최대
#
# 3. 진행 방식
#  - K개의 영어 소문자 조합을 combination으로 구하기
#  - 구한 값을 토대로, N개의 단어를 검사하기
#  
# 4. 시간복잡도
#  << a c i n t 제거 전 >>
#  - 3-1의 경우, 최대는 26C13이 될 것이다 --> 10,400,600
#  - 3-2의 경우, N개 검사 -->  문자열의 최대 길이 x 각 단어 개수 x 단어 검사하는 알파벳 개수 --> 15x50x13 =9750
#  - 10,400,600 x 9750 = 101,405,850,000
#  - 따라서 3-2에 대한 사전 작업이 필요할 듯 하다
#  --> 단어 합치기
#  --> a가 몇개인 지, b가 몇개인 지, 각각의 소문자를 counting한 array를 만든다
#  --> ex) arr = [0, 1, 2, 3, 4, 5, 6] : 총 단어에서 a가 0개, b가 1개, c가 2개, d가 3개, e가 4개 있다는 뜻
#  << a c i n t 제거 후 >>
#  - 3-1의 경우, 최대는 21C10이 최대가 될 것이다 --> 352716
#  - 3-2의 경우, 최대는 7x50x10 = 3500
#  - 계산해보면, 352716x3500 = 1,234,506,000
#  - set() 을 이용하여 검사를 해야 겠다
#  << a c i n t 제거 + 해당 알파벳 검사 set으로 검사 >>
#  - 알파벳 검사가 O(1)로 바뀐다
#  - (문자열 최대 길이 x 각 단어 개수) = 750
#  - 352716 x 750 = 264,537,000
#  ++ 앞의 단어보다 뒤의 단어를 더 세도 최댓값 갱신이 안 되면 stop하도록 짜야겠다 (추가 backtracking)
#  ++ 추후에 index를 만들어 계산값을 미리 저장 (a, b가 들어간 거면 2개다)
#
#
# @ 설계
#
# 1. 단어 array 만들기
#  - 앞, 뒤 제거하고 arr에 append
#
# 2. 검사할 알파벳 조합 만들기
#  - 빠르게 하기 위해 bit masking 활용 : a c i n t
#  - K개의 조합이라, bitmasking이 더 느리다
#  - 그냥 재귀 활용 combination으로 구현
#
# 3. 알파벳 조합 만들었으면, 검사 진행
#   3-1. a c i n t로 완성이 되는 지 (일종의 backtracking)
#   3-2. 나머지 apb 조합으로 완성이 되는 지
#
# 4. 읽을 수 있는 단어 최댓값 update
#


import sys
input = sys.stdin.readline

def combinations(step, idx, st:set = set()):
    global max_
    if (step == K_):
        can_read = 0
        for target in target_lst:
            if target <= st:
                can_read += 1
                
        max_ = max(max_, can_read)
        return
    
    for i in range(idx, len(apb_lst)):
        combinations(step+1, i+1, st | {apb_lst[i]})

N, K = map(int, input().split())
target_lst = []
apb_lst = ['b','d','e','f','g',
         'h','j','k','l','m',
         'o','p','q','r','s',
         'u','v','w','x','y',
         'z']
acint_set = set(['a','c','i','n','t'])

max_ = 0 # 읽는 최댓값

if (K < 5):
    print(0)
else:
    K_ = K-5
    
    for _ in range(N):
        tmp = set(map(str, input().rstrip()))
        target_lst.append(tmp-acint_set)
    
    combinations(0, 0)
    
    print(max_)
