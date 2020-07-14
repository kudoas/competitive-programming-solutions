n = int(input())
ans = n
for x in range(1, n+1):
    y = n//x
    if y < x:
        break
    score = (y-x) + (n-x*y)
    ans = min(ans, score)
print(ans)
