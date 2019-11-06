# a, b = map(int, input().split())
# print(a+b if a == b else max(a, b)+max(a, b)-1)

a = list(map(int, input().split()))
a.sort()
print(max(a[0], a[1])+max(a[0], a[1]-1))
