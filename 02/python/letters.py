file = open("input")

lines = []
for line in file:
    lines.append(line)
file.close()

twos = 0
threes = 0
for line in lines:
    counts = {}
    for char in line:
        if char in counts:
            counts[char] = counts[char] + 1
        else:
            counts[char] = 1
    if 2 in counts.values():
        twos = twos + 1
    if 3 in counts.values():
        threes = threes + 1
print twos * threes

def isdiff(a, b):
    if (a == b):
        return 0
    else: 
        return 1

for i in lines:
    for j in lines:
        if (sum(map(isdiff, i, j)) == 1):
            print i
