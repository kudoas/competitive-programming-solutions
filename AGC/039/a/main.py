import sys
import itertools
import math
input = sys.stdin.readline

ss = list(input().rstrip('\n'))
k = int(input())
cnt = 0
gr = itertools.groupby(ss)

# つなぎ目注意
ll = [[key, group] for key, group in gr]
if ll[1][0] == l[-1][0]:
    # hoge
else:
    # hoge
