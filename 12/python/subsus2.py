from sets import Set

file = open("input")

state = Set([])
linenum = 1
comb = {}
for line in file:
    if linenum == 1:
        st = line.split(": ")[1].strip()
        for i in range(len(st)):
            if st[i] == "#":
                state.add(i)
    if linenum >= 3:
        linesp = line.split(" => ")
        comb[line.split(" => ")[0]] = line.split(" => ")[1].strip()
    linenum += 1

def newgen(g, c):
    ng = Set(g)
    for plant in g:
        for step in range(5):
            co = ""
            for offset in range(5):
                if plant + offset - step in g:
                    co += "#"
                else:
                    co += "."
            if co in c:
                if c[co] == "#":
                    ng.add(plant + 2 - step)
                else:
                    if plant + 2 - step in g and plant + 2 - step in ng:
                        ng.remove(plant + 2 - step)
    return ng

#gens = 20
gens = 50000000000
history = Set([state])
while gens > 0:
    state = newgen(state, comb)
    gens -= 1
    if Set(map(lambda x: x - 1, state)) in history:
        answer = sum(state) + (gens * len(state))
        break
    answer = sum(state)
    history.add(state)

print answer
