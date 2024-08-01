A, B = map(int, input().split())

def bfs(number):
    if (A == B): return 0

    q = []
    q.append(number)

    step = 1
    curSize = 0

    # 모두 증가 조건이기 때문에, Queue에 무한히 쌓일 일은 없다
    while q:
        curSize = len(q)

        for c in range(curSize):
            target = q.pop(0)

            # 1번 과정 진행
            next_1 = target*2
            if (next_1 < 1e9):
                if (next_1 == B):
                    return step+1
                else:
                    q.append(next_1)

            # 2번 과정 진행
            next_2 = target*10 + 1
            if (next_2 < 1e9):
                if (next_2 == B):
                    return step+1
                else:
                    q.append(next_2)
        step += 1

    return -1

ans = bfs(A)

print(ans)