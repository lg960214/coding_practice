target = input()

cnt = 0

i = 0

while (i < len(target)):
    if (target[i] == 'c'):
        if (i >= len(target)-1): pass
        else:
            if (target[i+1] == '='):
                i += 1
            elif (target[i+1] == '-'):
                i += 1
    elif (target[i] == 'd'):
        if (i >= len(target)-1): pass
        else:
            if (target[i+1] == 'z'):
                if (i >= len(target)-2): pass
                else:
                    if (target[i+2] == '='):
                        i += 2
            elif (target[i+1] == '-'):
                i += 1
    elif (target[i] == 'l'):
        if (i >= len(target)-1): pass
        else:
            if (target[i+1] == 'j'):
                i += 1

    elif (target[i] == 'n'):
        if (i >= len(target)-1): pass
        else:
            if (target[i+1] == 'j'):
                i += 1
    elif (target[i] == 's'):
        if (i >= len(target)-1): pass
        else:
            if (target[i+1] == '='):
                i += 1
    elif (target[i] == 'z'):
        if (i >= len(target)-1): pass
        else:
            if (target[i+1] == '='):
                i += 1

    cnt += 1
    i += 1

print(cnt)