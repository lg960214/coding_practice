T = int(input())

for t in range(1, T+1):
    target = input()

    temp_target = ''

    for txt in target:
        if (txt in '{()}'):
            temp_target += txt

    while True:
        pos_1 = temp_target.find('{}')
        pos_2 = temp_target.find('()')
        if (pos_1 == -1 and pos_2 == -1): break

        if (pos_1 != -1):
            if (pos_1 == len(temp_target) - 2):
                temp_target = temp_target[:pos_1]
            else:
                temp_target = temp_target[:pos_1] + temp_target[pos_1 + 2:]
        elif (pos_2 != -1):
            if (pos_2 == len(temp_target) - 2):
                temp_target = temp_target[:pos_2]
            else:
                temp_target = temp_target[:pos_2] + temp_target[pos_2 + 2:]

    ans = 'YES' if (len(temp_target) == 0) else 'NO'
    print(f'{ans}')