import itertools

a = list(map(int, input().split()))
se = set(sum(sub) for sub in itertools.combinations(a, 3))
li = list(se)
li.sort(reverse=True)
print(li[2])
