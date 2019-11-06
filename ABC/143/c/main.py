n = int(input())
S = [s for s in input()]
ans = []

for i in range(n-1):
    if S[i] != S[i+1]:
        ans += S[i]

print(len(ans)+1)
