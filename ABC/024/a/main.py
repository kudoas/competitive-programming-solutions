a, b, c, k = map(int, input().split())
s, t = map(int, input().split())
# base = a*s+b*t
# print(base-(s+t)*c if s+t >= k else base)

print(a*s+b*t-(s+t)*c*(s+t >= k))
