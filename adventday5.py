import collections

# Plot all non-diagonal lines, answer is number of squares with > 1 line

INPUT_S = '''\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
7,0 -> 7,4
'''
points: collections.Counter[tuple[int, int]] = collections.Counter()

for line in INPUT_S.splitlines():
    start, end = line.split('->')
    x1_s, y1_s = start.split(',')
    x2_s, y2_s = end.split(',')
    x1, y1, x2, y2 = int(x1_s), int(y1_s), int(x2_s), int(y2_s)

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            points[(x1, y)] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            points[(x, y1)] += 1

count = 0

for k, v in points.most_common():
    if v > 1:
        count += 1
    else:
        break
print(count)

