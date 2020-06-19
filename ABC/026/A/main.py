a = int(input())
ans = 0
for i in range(a):
    ans = max(ans, i*(a-i))
print(ans)
