from itertools import product

n = int(input())
abc = ['abc']*n

for s in product(*abc):
    print(''.join(s))
