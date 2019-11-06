# import math

# n = int(input())
# a = list(map(int, input().split()))
# ave = sum(a)/(len(a)-a.count(0))

# print(math.ceil(ave))

n = int(input())
a = list(map(int, input().split()))

print(-(-sum(a)//(n-a.count(0))))
