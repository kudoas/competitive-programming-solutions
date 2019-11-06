all = dict()

all['a'] = [s for s in input()]
all['b'] = [s for s in input()]
all['c'] = [s for s in input()]

player = 'a'

while all[player]:
    player = all[player].pop()

print(player.upper())
