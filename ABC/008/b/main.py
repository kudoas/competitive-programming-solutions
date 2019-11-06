from collections import Counter

n = int(input())
ls = []

for _ in range(n):
    ls.append(input())

counter = Counter(ls)
print(counter.most_common()[0][0])
