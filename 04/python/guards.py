file = open("input")

events = []
for line in file:
    events.append(line.split(']'))

def getKey(item):
    return item[0]
events = sorted(events, key=getKey)

sleeps = {}
guard = -1
start = -1
stop = -1
for event in events:
    if event[1].startswith(" Guard"):
        guard = int(event[1].split()[1][1:])
    elif event[1].startswith(" falls"):
        start = int(event[0].split(":")[1])
    else:
        stop = int(event[0].split(":")[1])
        if guard not in sleeps:
            sleeps[guard] = [0] * 60
        for i in range(start, stop):
            sleeps[guard][i] = sleeps[guard][i] + 1

guardsleeps = []
for guard in sleeps:
    guardsleeps.append((guard, sum(sleeps[guard]))) # For part 2 use max function instead

mostsleepy = sorted(guardsleeps, key=lambda x: x[1], reverse=True)[0]
mostsleepyguard = mostsleepy[0]
mostsleepyminute = sleeps[mostsleepyguard].index(max(sleeps[mostsleepyguard]))
print mostsleepyguard * mostsleepyminute

