records = input()

scores = [[0, 0] for _ in range(9)]
scores.append([0, 0, 0])

bonus = [[1, 1] for _ in range(9)]
bonus.append([1, 1, 1])


i = 0
for frame in range(10):
    if frame < 9:
        for chance in range(2):
            record = records[i]
            if record.isdigit():
                scores[frame][chance] = int(record)
            else:
                if record == 'S':
                    scores[frame][0] = '-'
                    bonus[frame][0] = 0
                    scores[frame][1] = record
                    bonus[frame][1] = 1
                    i += 1
                    break
                else:
                    scores[frame][chance] = record
                    bonus[frame][chance] = 1
            i += 1
    else:
        lasts = list(records[i:])
        chance = 0
        while lasts:
            record = lasts.pop(0)
            if record.isdigit():
                scores[frame][chance] = int(record)
            else:
                scores[frame][chance] = record
            chance += 1
            i += 1
        break

for frame in range(9):
    for chance in range(2):
        record = scores[frame][chance]
        if record == 'P':
            count = 0
            if isinstance(scores[frame][chance - 1], int):
                scores[frame][chance] = 10 - scores[frame][chance - 1]
            else:
                scores[frame][chance] = 10
            for f in range(frame + 1, 10):
                for c in range(2):
                    if bonus[f][c]:
                         bonus[f][c] += 1
                         count += 1
                         break
                if count == 1:
                    break
        if record == 'S':
            count = 0
            scores[frame][chance] = 10
            for f in range(frame + 1, 10):
                for c in range(2):
                    if bonus[f][c]:
                         bonus[f][c] += 1
                         count += 1
                    if count == 2:
                        break
                if count == 2:
                    break
        elif record == '-':
            scores[frame][chance] = 0

for chance in range(3):
    record = scores[9][chance]
    if record == 'S':
        scores[9][chance] = 10
    elif record == 'P':
        if isinstance(scores[9][chance - 1], int):
            scores[9][chance] = 10 - scores[9][chance - 1]
        else:
            scores[9][chance] = 10
    elif isinstance(record, int):
        continue
    else:
        scores[9][chance] = 0
        
result = 0
for sc, bo in zip(scores, bonus):
    for s, b in zip(sc, bo):
        result += s * b
print(result)
