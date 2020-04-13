from math import gcd

k = int(input())
IJ = []

cnt = 0
for i in range(1, k+1):
    for j in range(1, k+1):
        IJ.append(gcd(i, j))

for ij in IJ:
    for k in range(1, k+1):
        cnt += gcd(ij, k)

print(cnt)
