money = 300
items = [['orange', 100], ['apple', 200], ['grape', 300]]
n = len(items)

for i in range(2**n):
    bag = []
    total = 0
    for j in range(n):
        if ((i >> j) & 1):
            bag.append(items[j][0])
            total += items[j][1]
    if total <= money:
        print(total, bag)
