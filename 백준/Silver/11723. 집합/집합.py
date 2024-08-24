import sys

input = sys.stdin.readline



N = int(input())

init_ = set()

for i in range(N):
    cmd = input().split()
    try:
        num = int(cmd[1])
    except:
        pass

    if cmd[0] == 'add':
        init_.add(num)
    elif cmd[0] == 'remove':
        if num in init_:
            init_.remove(num)
    elif cmd[0] == 'check':
        if num in init_:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        if num in init_:
            init_.remove(num)
        else:
            init_.add(num)
    elif cmd[0] == 'all':
        init_ = set(range(1, 21))
    elif cmd[0] == 'empty':
        init_ = set()
