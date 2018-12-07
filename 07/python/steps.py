from sets import Set

file = open("input-test")

steps = []
for line in file:
    step = line.split()
    todo = step[1]
    before = step[7]
    steps.append((todo, before))

allsteps = Set()
for step in steps:
    allsteps.add(step[0])
    allsteps.add(step[1])

def findfirststeps():
    availablesteps = Set()
    for step in allsteps:
        if step not in before :
            availablesteps.add(step)
    return sorted(availablesteps)

def findnextsteps(done):
    availablesteps = Set()
    remsteps = filter(lambda x: x[0] not in done, steps)
    unsatisfied = map(lambda x: x[1], remsteps)
    for step in allsteps:
        if step not in done and step not in unsatisfied:
                availablesteps.add(step)
    return sorted(availablesteps)


before = Set(map(lambda x: x[1], steps))
todos = Set(map(lambda x: x[0], steps))

elves = {}
for i in range(5):
    elves[i] = (".", 0)
print elves
order = []
nextsteps = findfirststeps()
inprogress = Set()
time = 0
while (len(nextsteps) > 0):
    for elf in elves:
        if elves[elf][1] <= time:
            if elves[elf][0] != ".":
                inprogress.remove(elves[elf][0])
                order.append(elves[elf][0])
            elves[elf] = (nextsteps[0], 60)
            inprogress.add(nextsteps[0])
            break
    nextsteps = findnextsteps(order)
    time += 1

print elves
print "".join(order)
