from sets import Set

file = open("input")

class Cart:
    x = -1
    y = -1
    direction = '.'
    covers = '.'
    juncdir = 'L'

    def __init__(self, x, y, direction, covers):
        self.x = x
        self.y = y
        self.direction = direction
        self.covers = covers

    def move(self, tracks):
        if self.direction == 'v':
            self.y += 1
            self.covers = tracks[self.y][self.x]
            if self.covers == '\\':
                self.direction = '>'
            elif self.covers == '/':
                self.direction = '<'
        elif self.direction == '^':
            self.y -= 1
            self.covers = tracks[self.y][self.x]
            if self.covers == '\\':
                self.direction = '<'
            elif self.covers == '/':
                self.direction = '>'
        elif self.direction == '<':
            self.x -= 1
            self.covers = tracks[self.y][self.x]
            if self.covers == '\\':
                self.direction = '^'
            elif self.covers == '/':
                self.direction = 'v'
        elif self.direction == '>':
            self.x += 1
            self.covers = tracks[self.y][self.x]
            if self.covers == '\\':
                self.direction = 'v'
            elif self.covers == '/':
                self.direction = '^'
        if self.covers == '+':
            self.turn()
    
    def turn(self):
        if self.direction == '^':
            if self.juncdir == 'L':
                self.direction = '<'
                self.juncdir = 'S'
            elif self.juncdir == 'R':
                self.direction = '>'
                self.juncdir = 'L'
            else:
                self.juncdir = 'R'
        elif self.direction == 'v':
            if self.juncdir == 'L':
                self.direction = '>'
                self.juncdir = 'S'
            elif self.juncdir == 'R':
                self.direction = '<'
                self.juncdir = 'L'
            else:
                self.juncdir = 'R'
        elif self.direction == '<':
            if self.juncdir == 'L':
                self.direction = 'v'
                self.juncdir = 'S'
            elif self.juncdir == 'R':
                self.direction = '^'
                self.juncdir = 'L'
            else:
                self.juncdir = 'R'
        elif self.direction == '>':
            if self.juncdir == 'L':
                self.direction = '^'
                self.juncdir = 'S'
            elif self.juncdir == 'R':
                self.direction = 'v'
                self.juncdir = 'L'
            else:
                self.juncdir = 'R'

    def occupies(self, x, y):
        return self.x == x and self.y == y

    def __str__(self):
        return ''.join(["x: ", str(self.x), ", y: ", str(self.y), ", dir: ", self.direction, ", covers: ", self.covers])

tracks = []
carts = []
y = 0
for line in file:
    x = 0
    row = []
    for ch in line.rstrip("\n"):
        if ch == '<' or ch == '>':
            carts.append(Cart(x, y, ch, '-'))
            row.append('-')
        elif ch == '^' or ch == 'v':
            carts.append(Cart(x, y, ch, '|'))
            row.append('|')
        else:
            row.append(ch)
        x += 1
    y += 1

    tracks.append(row)

def printcarts(carts):
    for cart in carts:
        print cart

def printtracks(t):
    for row in t:
        print "".join(row)

def iscollision(carts):
    return len(Set(map(lambda x: (x.x, x.y), carts))) != len(carts)

def cartorder(a, b):
    if a.y == b.y:
        return a.x - b.x
    return a.y - b.y

while len(carts) > 1:
    carts.sort(cmp=cartorder)
    allremove = Set([])
    for cart in carts:
        cart.move(tracks)
        if iscollision(carts):
            print ''.join(["Collision: ", str(cart.x), ',', str(cart.y)])
            allremove.add((cart.x, cart.y))
        carts = filter(lambda c: (c.x, c.y) not in allremove, carts)
printcarts(carts)
