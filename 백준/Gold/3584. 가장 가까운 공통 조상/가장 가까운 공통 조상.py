T = int(input())

for t in range(1, T+1):
    N = int(input())

    parents = dict()

    for _ in range(N-1):
        v1, v2 = list(map(int, input().split()))
        parents[v2] = v1

    A, B = list(map(int, input().split()))

    v1_parents = [A]
    v2_parents = [B]

    while True:
        if (parents.get(A) == None):
            break
        A = parents[A]
        v1_parents.append(A)


    while True:
        if (parents.get(B) == None):
            break
        B = parents[B]
        v2_parents.append(B)


    for i in range(len(v1_parents)):
        common = v1_parents[i]
        if (common in v2_parents):
            print(common)
            break
    else:
        print(1)