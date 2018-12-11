input = 7857

gridsize = 300
rack = []
for y in range(gridsize):
    row = []
    for x in range(gridsize):
        xs = x + 1
        ys = y + 1
        rackid = xs + 10
        startpower = (rackid * ys + input) * rackid
        p = str(startpower)
        if len(p) >= 3:
            power = p[len(p) - 3]
        else:
            power = '0'
        row.append(int(power) - 5)
    rack.append(row)

total = ()
maxsum = -5 * 9
#for sq in range(3, 4):
for sq in range(1, 301):
    for y in range(gridsize - sq):
        for x in range(gridsize - sq):
            p = 0
            for v in range(y, y + sq):
                for h in range(x, x + sq):
                    p += rack[v][h]
            if p > maxsum:
                total = (x + 1,y + 1,sq)
                print total
                maxsum = p
print total
