file = open("input")

points = []
for line in file:
    pos = map(lambda x: int(x), line.strip().split('>')[0].split('<')[1].split(','))
    vel = map(lambda x: int(x), line.strip().split('>')[1].split('<')[1].split(','))
    points.append([pos, vel])

def minx(x,y):
    if x[0][0] < y[0][0]:
        return x
    return y

def maxx(x,y):
    if x[0][0] > y[0][0]:
        return x
    return y

def miny(x,y):
    if x[0][1] < y[0][1]:
        return x
    return y

def maxy(x,y):
    if x[0][1] > y[0][1]:
        return x
    return y

def printgrid(g):
    for row in g:
        for col in row:
            print col,
        print

def applypoints(ps):
    mnx = reduce(lambda x, y: minx(x, y), points)[0][0]
    mxx = reduce(lambda x, y: maxx(x, y), points)[0][0]
    mny = reduce(lambda x, y: miny(x, y), points)[0][1]
    mxy = reduce(lambda x, y: maxy(x, y), points)[0][1]
    grid = []
    if len(range(mny, mxy)) < 10:
        grid = [["." for i in range(mnx, mxx + 1)] for j in range(mny, mxy + 1)]
        for p in ps:
            grid[p[0][1] - mny][p[0][0] - mnx] = "#"
    return grid

def tickpoints(ps):
    for p in ps:
        p[0][0] += p[1][0]
        p[0][1] += p[1][1]
    return ps

iter = 0
while True:
    grid = applypoints(points)
    if len(grid) > 0:
        print iter
        printgrid(grid)
    points = tickpoints(points)
    iter += 1

