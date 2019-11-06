s = input()
n = len(s) - 1

for i in range(2**n):
    S = s[0]
    for j in range(n):
        if ((i >> j) & 1):
            S += '+'
        else:
            S += '-'
        S += s[j+1]
        if len(S) == 7 and eval(S) == 7:
            print(S+'=7')
            exit()
