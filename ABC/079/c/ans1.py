abcd = input()
n = len(abcd)-1

for i in range(2**n):
    ope = ['-']*n
    for j in range(n):
        if (i >> j & 1):
            ope[j] = '+'
    formula = ''
    for i, o in zip(abcd, ope+['']):
        formula += i+o
    if eval(formula) == 7:
        print(formula+'=7')
        break
