target = input()

for i in range(len(target)//2):
    if (target[i] != target[len(target)-1-i]):
        print(0)
        break
else:
    print(1)