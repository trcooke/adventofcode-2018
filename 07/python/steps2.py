from sets import Set
from string import ascii_uppercase

file = open("input")

nodes = {}
for line in file:
    line = line.split()
    if line[1] not in nodes:
        nodes[line[1]] = (Set(), Set(line[7]))
    else:
        nodes[line[1]][1].add(line[7])
    if line[7] not in nodes:
        nodes[line[7]] = (Set(line[1]), Set())
    else:
        nodes[line[7]][0].add(line[1])

allnodes = nodes.keys()

basetime = 60
times = {}
t = 1
for c in ascii_uppercase:
    times[c] = basetime + t
    t += 1

workers = []
for i in range(5):
    workers.append(["Idle", ".", 0, i])

def removeblocking(nodes, nextwork):
    blockednodes = filter(lambda x: nextwork in nodes[x][0] , nodes)
    for blockednode in blockednodes:
        nodes[blockednode][0].remove(nextwork)
    return nodes

def idleworkers(ws):
    return filter(lambda x: x[0] == "Idle", ws)

def finishedworkers(ws):
    return filter(lambda x: x[0] == "Busy" and x[2] == 0, ws)

def tickworkers(ws):
    for w in ws:
        if w[0] == "Busy":
            w[2] = w[2] - 1

timer = 0
done = []
while len(done) != len(allnodes):
    nextwork = sorted(filter(lambda x: len(nodes[x][0]) == 0, nodes))
    finished = finishedworkers(workers)
    for f in finished:
        done.append(f[1])
        nodes = removeblocking(nodes, f[1])
        f[0] = "Idle" 
        f[1] = "."
        f[2] = 0
    nextwork = sorted(filter(lambda x: len(nodes[x][0]) == 0, nodes))
    for n in nextwork:
        idle = idleworkers(workers)
        if len(idle) > 0:
            idle[0][0] = "Busy" 
            idle[0][1] = n
            idle[0][2] = times[n]
            nodes.pop(n)
    tickworkers(workers)
    timer += 1

print "".join(done)
print timer - 1
