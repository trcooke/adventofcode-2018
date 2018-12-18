input = 30121
#inputstr = str(030121)
#input = 9
inputstr = "030121"
#input = 5
#input = 18
#input = 2018

recipes = [3, 7]
elf1 = 0
elf2 = 1

while len(recipes) < input + 10:
    elf1score = recipes[elf1]
    elf2score = recipes[elf2]
    scoresum = elf1score + elf2score
    scoredigits = map(lambda x: int(x), list(str(scoresum)))
    recipes.extend(scoredigits)
    elf1 = (elf1 + 1 + elf1score) % len(recipes)
    elf2 = (elf2 + 1 + elf2score) % len(recipes)

print ''.join(map(str, recipes[input:input+10]))

recipes = [3, 7]
elf1 = 0
elf2 = 1

more = True
while more:
    elf1score = recipes[elf1]
    elf2score = recipes[elf2]
    scoresum = elf1score + elf2score
    scoredigits = map(lambda x: int(x), list(str(scoresum)))
    recipes.extend(scoredigits)
    elf1 = (elf1 + 1 + elf1score) % len(recipes)
    elf2 = (elf2 + 1 + elf2score) % len(recipes)

    recipestr = ''.join(map(str, recipes[len(recipes) - len(scoredigits) - 6:]))
    foundi = recipestr.find(inputstr)
    if foundi != -1:
        print foundi + len(recipes) - len(scoredigits) - 6
        more = False
