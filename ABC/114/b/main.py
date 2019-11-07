s = [int(i) for i in input()]
n = len(s)-1
ans = float('inf')

for i in range(n-1):
    abc = 100*s[i]+10*s[i+1]+s[i+2]
    ans = min(ans, abs(abc-753))

print(ans)
