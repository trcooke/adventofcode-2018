from sets import Set

changes = open("input")

freqs = []
for line in changes:
    freqs.append(int(line))

final_freq = 0
for freq in freqs:
    final_freq = final_freq + freq

print final_freq

seen = Set([0])
final = 0
keep_going = True
while keep_going:
    for freq in freqs:
        final = final + freq
        if final in seen:
            print final
            keep_going = False
            break
        seen.add(final)
