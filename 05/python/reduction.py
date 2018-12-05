from string import ascii_lowercase

file = open("input")

polymers = list(file.read().strip())

def react(polymers):
    reacted = []
    for polymer in polymers:
        if len(reacted) == 0:
            reacted.append(polymer)
            continue
        lastreacted = reacted.pop()
        if (polymer.upper() == lastreacted.upper()) and (polymer.isupper() != lastreacted.isupper()):
            continue
        else:
            reacted.append(lastreacted)
            reacted.append(polymer)
    return reacted

print len(react(polymers))

file = open("input")
polymers = list(file.read().strip())

minlen = len(polymers)
for c in ascii_lowercase:
    filtered = filter(lambda x: x.lower() != c, polymers)
    thislen = len(react(filtered))
    if (thislen < minlen):
        minlen = thislen
print minlen
