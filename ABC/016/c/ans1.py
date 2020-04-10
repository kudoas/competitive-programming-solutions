n, m = map(int, input().split())
relation = [None] + [[]for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

for i in range(1, n+1):
    friends = relation[i]
    ans = set()
    for friend in friends:
        ans |= set(relation[friend])
    ans -= set(friends) | {i}
    print(len(ans))
