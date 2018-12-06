from sets import Set
from collections import Counter

file = open("input")

coords = []
index = 1
for line in file:
    [x,y] = map(lambda x: int(x), line.strip().split(", "))
    coords.append((str(index), x, y))
    index += 1

xmax = max(coords, key=lambda x: x[1])[1] + 1
ymax = max(coords, key=lambda x: x[2])[2] + 1

lessthou = 0

def mindist((xin, yin), cs):
    mindist = xmax + ymax
    closest = "."
    alldist = 0
    for coord in cs:
        dist = abs(xin - coord[1]) + abs(yin - coord[2])
        alldist += dist
        if dist < mindist:
            mindist = dist
            closest = coord[0]
        elif dist == mindist:
            closest = "."
    return (closest, alldist)

grid = [["." for i in range(xmax)] for j in range(ymax)]
for yi in range(ymax):
    for xi in range(xmax):
        (closest, alldist) = mindist((xi,yi), coords)
        grid[yi][xi] = closest
        if alldist < 10000:
            lessthou += 1

#for row in grid:
#    print row

infinites = Set()
for item in grid[0]:
    if item != ".":
        infinites.add(item)

for item in grid[ymax - 1]:
    if item != ".":
        infinites.add(item)

for item in grid:
    if item[0] != ".":
        infinites.add(item[0])
    if item[xmax - 1] != ".":
        infinites.add(item[xmax - 1])

flat = [item for sublist in grid for item in sublist]
final = filter(lambda x: x != ".",flat)
final = filter(lambda x: x not in infinites, final)
print Counter(final).most_common()[0][1]
print lessthou
