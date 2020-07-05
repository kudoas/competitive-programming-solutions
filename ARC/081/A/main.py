from collections import defaultdict

n = int(input())
A = map(int, input().split())
C = defaultdict(int)
for a in A:
    C[a] += 1
C = sorted(C.items(), key=lambda x: x[0], reverse=True)
rods = []
for k, v in C:
    if v >= 4:
        rods.append(k)
        rods.append(k)
        break
    if v >= 2:
        rods.append(k)
    if len(rods) == 2:
        break
if len(rods) >= 2:
    ans = rods[0]*rods[1]
else:
    ans = 0
print(ans)
