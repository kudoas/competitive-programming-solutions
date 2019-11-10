import sys
input = sys.stdin.readline

n = int(input())
dd = list(map(int, input().split()))
dd.sort()
ls = []
ans = 1

for i in range(n):
    cnt = dd[:i].count(max(dd[:i+1])-1)
    ls.append(cnt)
    if max(ls)+1 >= dd[i]:
        ans *= max(cnt, 1)
    else:
        print(0)
        exit()

print(ans % 998244353)
