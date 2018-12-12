file = open("input")

state = []
linenum = 1
comb = {}
for line in file:
    if linenum == 1:
        state = line.split(": ")[1].strip()
    if linenum >= 3:
        linesp = line.split(" => ")
        comb[line.split(" => ")[0]] = line.split(" => ")[1].strip()
    linenum += 1

firsti = 0
def generate(s, c, firsti):
    s = "".join(["....", s])
    s = "".join([s, "...."])
    firsti -= 4
    nexts = list(s)
    
    for i in range(len(s) - 4):
        search = "".join(s[i:i+5])
        if search in c:
            nexts = "".join(["".join(nexts[:i+2]), c[search], "".join(nexts[i+3:])])

    ld = 0
    for i in range(len(nexts)):
        if nexts[i] == "#":
            break
        ld += 1
    firsti += ld
    nexts = nexts[ld:]
    return (nexts.rstrip("."), firsti)

g = 20
#g = 50000000000
history = [state]
i = 1
while i <= g:
    (state, firsti) = generate(state, comb, firsti)
    if (state, firsti) in history:
        print ("Repeated after ", i)
        break
    history.append((state, firsti))
    i += 1

finalstate = history[g % i]

s = 0
for i in range(len(finalstate[0])):
    if finalstate[0][i] == "#":
        s += (finalstate[1] + i)

print s
