n = int(input())
se = set()

for i in range(100):
    for j in range(100):
        se.add(i*7+j*4)

print('Yes' if n in se else 'No')
