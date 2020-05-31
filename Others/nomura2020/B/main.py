T = list(input())
n = len(T)
for i in range(n):
    if T[i] == '?':
        T[i] = 'D'
print(*T, sep='')
