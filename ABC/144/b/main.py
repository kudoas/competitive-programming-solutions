n = int(input())
ls = []
for i in range(1, 10):
    for j in range(1, 10):
        ls.append(i*j)

print('Yes' if n in ls else 'No')
