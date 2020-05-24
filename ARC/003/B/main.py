n = int(input())
d = {}
for i in range(n):
    d[i] = input()
b = {}
for k, v in d.items():
    b[k] = v[::-1]
b = sorted(b.items(), key=lambda x: x[1])
for ls in b:
    print(d[ls[0]])
