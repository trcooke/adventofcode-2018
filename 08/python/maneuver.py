from collections import deque

file = open("input")

nav = deque(file.read().strip().split())

def countmeta(q, cm):
    if len(q) == 0:
        return cm
    children = int(q.popleft())
    meta = int(q.popleft())
    cmc = 0
    for c in range(children):
        cmc += countmeta(q, cm)
    cm += cmc
    for m in range(meta):
        cm += int(q.popleft())
    return cm

print countmeta(nav, 0)


