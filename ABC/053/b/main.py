s = list(input())

A = s.index('A')
Z = len(s)-s[::-1].index('Z')

print(Z-A)
