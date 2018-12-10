from collections import deque

instructions = open("input").read().split()

numplayers = int(instructions[0])
lastmarble = int(instructions[6]) * 100

circle = deque([0])
turn = 1

scores = {}

while turn <= lastmarble:
    if turn % 23 == 0:
        scores[turn % numplayers] = scores.get(turn % numplayers, 0) + turn
        circle.rotate(7)
        scores[turn % numplayers] = scores.get(turn % numplayers) + circle.popleft()
    else:
        circle.rotate(-2)
        circle.appendleft(turn)
    turn += 1

print max(scores.values())
