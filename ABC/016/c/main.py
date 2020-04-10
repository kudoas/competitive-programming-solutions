n, m = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(m)]
AB.sort()

for i in range(1, n+1):
    friends = set([])
    fri_friends = set([])
    for j in range(m):
        if AB[j][0] == i or AB[j][1] == i:
            friends.add(AB[j][0])
            friends.add(AB[j][1])
    for j in range(m):
        if AB[j][0] in friends and AB[j][1] in friends:
            continue
        if AB[j][0] in friends or AB[j][1] in friends:
            if AB[j][0] in friends:
                fri_friends.add(AB[j][1])
            else:
                fri_friends.add(AB[j][0])
    print(len(fri_friends))
