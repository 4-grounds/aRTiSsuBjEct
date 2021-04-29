import random

x = "2 + 2 ="

y = ("3", "5", "88", "nothing", "16", "mafia", "the legend of zelda: breath of the wild")

i = random.choice(y)

print(x, i)

""" this way works too but it takes too many lines
w = len(y)

z = random.randint(0 - 1, w - 1)

i = y[z]
"""