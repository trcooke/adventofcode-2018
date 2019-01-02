file = open('inputp1')

lines = file.readlines()
file.close()
def addr(r, i):
    after = [r[0], r[1], r[2], r[3]]
    after[i[3]] = r[i[1]] + r[i[2]]
    return after

def addi(r, i):
    after = [r[0], r[1], r[2], r[3]]
    after[i[3]] = r[i[1]] + i[2]
    return after

def mulr(r, i):
    after = [r[0], r[1], r[2], r[3]]
    after[i[3]] = r[i[1]] * r[i[2]]
    return after

def muli(r, i):
    after = [r[0], r[1], r[2], r[3]]
    after[i[3]] = r[i[1]] * i[2]
    return after

def banr(r, i):
    after = [r[0], r[1], r[2], r[3]]
    after[i[3]] = r[i[1]] & r[i[2]]
    return after

def bani(r, i):
    after = [r[0], r[1], r[2], r[3]]
    after[i[3]] = r[i[1]] & i[2]
    return after

def borr(r, i):
    after = [r[0], r[1], r[2], r[3]]
    after[i[3]] = r[i[1]] | r[i[2]]
    return after

def bori(r, i):
    after = [r[0], r[1], r[2], r[3]]
    after[i[3]] = r[i[1]] | i[2]
    return after

def setr(r, i):
    after = [r[0], r[1], r[2], r[3]]
    after[i[3]] = r[i[1]]
    return after

def seti(r, i):
    after = [r[0], r[1], r[2], r[3]]
    after[i[3]] = i[1]
    return after

def gtir(r, i):
    after = [r[0], r[1], r[2], r[3]]
    if i[1] > r[i[2]]:
        after[i[3]] = 1
    else:
        after[i[3]] = 0
    return after

def gtri(r, i):
    after = [r[0], r[1], r[2], r[3]]
    if r[i[1]] > i[2]:
        after[i[3]] = 1
    else:
        after[i[3]] = 0
    return after

def gtrr(r, i):
    after = [r[0], r[1], r[2], r[3]]
    if r[i[1]] > r[i[2]]:
        after[i[3]] = 1
    else:
        after[i[3]] = 0
    return after

def eqir(r, i):
    after = [r[0], r[1], r[2], r[3]]
    if i[1] == r[i[2]]:
        after[i[3]] = 1
    else:
        after[i[3]] = 0
    return after

def eqri(r, i):
    after = [r[0], r[1], r[2], r[3]]
    if r[i[1]] == i[2]:
        after[i[3]] = 1
    else:
        after[i[3]] = 0
    return after

def eqrr(r, i):
    after = [r[0], r[1], r[2], r[3]]
    if r[i[1]] == r[i[2]]:
        after[i[3]] = 1
    else:
        after[i[3]] = 0
    return after

examples = []

opcodes = {}
examples = []
while lines != []:
    poss = []
    before = map(int, lines.pop(0).strip().split(':')[1].strip(' []').split(','))
    instruction = map(int, lines.pop(0).strip().split(' '))
    after = map(int, lines.pop(0).strip().split(':')[1].strip(' []').split(','))
    if lines != []:
        lines.pop(0)
    if addr(before, instruction) == after:
        poss.append('addr')
    if addi(before, instruction) == after:
        poss.append('addi')
    if mulr(before, instruction) == after:
        poss.append('mulr')
    if muli(before, instruction) == after:
        poss.append('muli')
    if banr(before, instruction) == after:
        poss.append('banr')
    if bani(before, instruction) == after:
        poss.append('bani')
    if borr(before, instruction) == after:
        poss.append('borr')
    if bori(before, instruction) == after:
        poss.append('bori')
    if setr(before, instruction) == after:
        poss.append('setr')
    if seti(before, instruction) == after:
        poss.append('seti')
    if gtir(before, instruction) == after:
        poss.append('gtir')
    if gtri(before, instruction) == after:
        poss.append('gtri')
    if gtrr(before, instruction) == after:
        poss.append('gtrr')
    if eqir(before, instruction) == after:
        poss.append('eqir')
    if eqri(before, instruction) == after:
        poss.append('eqri')
    if eqrr(before, instruction) == after:
        poss.append('eqrr')
    examples.append((instruction[0], poss))

print len(filter(lambda x: len(x[1]) >= 3, examples))

while len(opcodes) < 16:
    for example in examples:
        if len(example[1]) == 1:
            opcodes[example[0]] = example[1][0]
    for code in opcodes.values():
        for ex in examples:
            if code in ex[1]:
                ex[1].remove(code)
print opcodes

def execute(r, i):
    func = opcodes[i[0]]
    if func == 'addr':
        return addr(r,i)
    elif func == 'addi':
        return addi(r,i)
    elif func == 'mulr':
        return mulr(r,i)
    elif func == 'muli':
        return muli(r,i)
    elif func == 'banr':
        return banr(r,i)
    elif func == 'bani':
        return bani(r,i)
    elif func == 'borr':
        return borr(r,i)
    elif func == 'bori':
        return bori(r,i)
    elif func == 'setr':
        return setr(r,i)
    elif func == 'seti':
        return seti(r,i)
    elif func == 'gtir':
        return gtir(r,i)
    elif func == 'gtri':
        return gtri(r,i)
    elif func == 'gtrr':
        return gtrr(r,i)
    elif func == 'eqir':
        return eqir(r,i)
    elif func == 'eqri':
        return eqri(r,i)
    elif func == 'eqrr':
        return eqrr(r,i)
    return r

file = open("inputp2")
register = [0,0,0,0]
for line in file:
    instruction = map(int, line.strip().split(' '))
    register = execute(register, instruction)

print register[0]
