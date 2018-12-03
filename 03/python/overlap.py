from sets import Set

file = open("input")

squares = Set([])
multis = Set([])
lines = []
for line in file:
    lines.append(line)
    [name, coords] = line.split('@')
    [start, size] = coords.split(':')
    [x,y] = map(lambda x: int(x), start.strip().split(','))
    [w,h] = map(lambda x: int(x), size.strip().split('x'))
    for i in range(w):
        for j in range(h):
            cell = (x + i, y + j)
            if cell in squares:
                multis.add(cell)
            else:
                squares.add(cell)

for line in lines:
    [name, coords] = line.split('@')
    [start, size] = coords.split(':')
    [x,y] = map(lambda x: int(x), start.strip().split(','))
    [w,h] = map(lambda x: int(x), size.strip().split('x'))
    overlap = False
    for i in range(w):
        for j in range(h):
            cell = (x + i, y + j)
            if cell in multis:
                overlap = True
    if not overlap:
        print name

print len(multis)


