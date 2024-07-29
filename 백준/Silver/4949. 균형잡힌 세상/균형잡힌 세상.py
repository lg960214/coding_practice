while True:
    target = input()

    if (target == '.'):
        break

    stk = []
    flag = True
    for i in range(len(target)):
        if target[i] in ['(', '[']:
            stk.append(target[i])
        elif target[i] in [']', ')']:
            if not stk:
                flag = False
                break
            if (stk[-1] == '[' and target[i] == ']'):
                stk.pop()
            elif (stk[-1] == '(' and target[i] == ')'):
                stk.pop()
            else:
                flag = False
                break
    else:
        if (stk):
            flag = False
            
    if (flag):
        print('yes')
    else:
        print('no')