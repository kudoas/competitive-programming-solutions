ls = list(map(int, input().split()))
ans = []

for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            ans.append(ls[i]+ls[j]+ls[k])

print(sorted(ans, reverse=True)[2])
