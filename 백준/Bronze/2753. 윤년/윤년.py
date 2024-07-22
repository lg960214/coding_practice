target = int(input())

if ((target % 4 == 0 and target % 100 != 0) or target % 400 == 0):
    print("1")
else:
    print('0')