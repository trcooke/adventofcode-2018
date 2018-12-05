from string import ascii_lowercase

file = open("input-test")

polymers = file.read().strip()

def react(polymers):
    more = True
    while more:
        more = False
        for i, val in enumerate(polymers):
            if i == 0:
                continue
            if (polymers[i-1].upper() == val.upper()) and (polymers[i-1].isupper() != val.isupper()):
                polymers = polymers[0:i-1]+polymers[i+1:]
                more = True
                break
    return polymers

#print len(react(polymers))

file = open("input")
polymers = file.read().strip()

minlen = len(polymers)
for c in ascii_lowercase:
    filtered = filter(lambda x: x.lower() != c, polymers)
    thislen = len(react(filtered))
    if (thislen < minlen):
        minlen = thislen
print minlen
