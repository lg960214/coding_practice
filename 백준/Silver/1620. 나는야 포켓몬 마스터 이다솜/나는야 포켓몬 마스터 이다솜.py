N, M = map(int, input().split())

dict_1 = dict()
dict_2 = dict()

for i in range(1, N+1):
    tmp = input()
    dict_1[i] = tmp
    dict_2[tmp] = i

for j in range(M):
    tmp = input()
    try:
        tmp = int(tmp)
        print(dict_1[tmp])
    except:
        print(dict_2[tmp])