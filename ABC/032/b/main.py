from collections import defaultdict

s = input()
k = int(input())
d = defaultdict(int)

if len(s) < k:
    print(0)
    exit()

for i in range(len(s)-k+1):
    d[s[i:i+k]] += 1

print(len(d))
