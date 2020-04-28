n = int(input())
s = input()
dp_L = [0]*(n+1)
dp_R = [0]*(n+1)

for i in range(n):
    dp_L[i+1] = dp_L[i]+[0, 1][s[i] == 'W']

for i in reversed(range(n)):
    dp_R[i] = dp_R[i+1]+[0, 1][s[i] == 'E']

print(min(L+R for L, R in zip(dp_L, dp_R)))
