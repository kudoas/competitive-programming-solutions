import sys
input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))
d.sort()

l = len(d)//2
print(0 if d[l-1] == d[l] else d[l]-d[l-1])
