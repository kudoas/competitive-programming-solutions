# n = int(input())
# alp = "abcdefghijklmnopqrstuvwxyz"
# ans = []


# def dfs(s):
#     if len(s) == n:
#         ans.append(s)
#         return 0
#     se = len(set(s))
#     for i in range(se+1):
#         dfs(s+alp[i])


# dfs('a')
# print(*ans, sep='\n')

import sys
sys.setrecursionlimit(10**7)
n = int(input())


def dfs(s):
    if len(s) == n:
        print(s)
        return 0
    for x in map(chr, range(97, ord(max(s))+2)):
        dfs(s+x)


dfs('a')
