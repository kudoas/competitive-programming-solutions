#! /usr/bin/env python3
n, l = map(int, input().split())
s = sorted([input() for i in range(n)])
print(*s, sep="")
