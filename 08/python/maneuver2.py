from collections import deque

file = open("input")

nav = deque(file.read().strip().split())

tree = ()

def nodes(q):
    children = int(q.popleft())
    meta = int(q.popleft())
    cmc = 0
    cs = []
    for c in range(children):
        cs.append(nodes(q))
    ms = []
    for m in range(meta):
        ms.append(int(q.popleft()))
    return (cs, ms)

tree = nodes(nav)

def summeta(node):
    tm = 0
    for c in node[0]:
        tm += summeta(c)
    for m in node[1]:
        tm += m
    return tm

print summeta(tree)

def summeta2(node):
    tm = 0
    if len(node[0]) > 0:
        for m in node[1]:
            if m <= len(node[0]):
                tm += summeta2(node[0][m - 1])
    else:
        for m in node[1]:
            tm += m
    return tm

print summeta2(tree)
