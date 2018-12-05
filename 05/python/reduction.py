from string import ascii_lowercase

file = open("input")

polymers = list(file.read().strip())

def react(polymers):
    more = True
    start = 0
    length = len(polymers)
    while more:
        more = False
        for i in range(start, length - 1):
            if (polymers[i].upper() == polymers[i+1].upper()) and (polymers[i].isupper() != polymers[i+1].isupper()):
                del polymers[i:i+2]
                #polymers = polymers[0:i-1]+polymers[i+1:]
                more = True
                if i > 0:
                    start = i - 1
                length = length - 2
                break
    return polymers

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
