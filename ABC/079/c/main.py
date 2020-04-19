abcd = list(map(int, input()))
n = len(abcd)-1


for i in range(2**n):
    ans = 0
    formula = []
    for j in range(n):
        if (i >> j & 1):
            formula.append('+')
        else:
            formula.append('-')
    ans += abcd[0]
    for k in range(n):
        if formula[k] == '+':
            ans += abcd[k+1]
        elif formula[k] == '-':
            ans -= abcd[k+1]
    if ans == 7:
        print(abcd[0], formula[0], abcd[1], formula[1],
              abcd[2], formula[2], abcd[3], '=', 7, sep='')
        break
