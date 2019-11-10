import sys
input = sys.stdin.readline

n = int(input())
dd = list(map(int, input().split()))
ans = 1
first = dd.pop(0)

if first != 0:
    print(0)
    exit()

for i in range(n-1):
    ans *= dd[i]

print(ans % 998244353)
