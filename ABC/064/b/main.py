n = int(input())
aa = list(map(int, input().split()))
aa.sort()

print(aa[-1]-aa[0])
