ls = list(input())

total = 0
s1 = []
s2 = []
for i in range(len(ls)):
    if ls[i] == '\\':
        s1.append(i)
    elif ls[i] == '/' and len(s1) > 0:
        j = s1.pop()
        area = i - j
        total += area

        while (len(s2) > 0 and s2[-1][0] > j):
            area += s2[-1][1]
            s2.pop()
        s2.append([j, area])


print(total)
print(len(s2), *[b for a, b in s2])
