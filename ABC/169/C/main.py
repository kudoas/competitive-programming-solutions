from math import floor
import decimal

a, b = input().split()
a = decimal.Decimal(a)
b = decimal.Decimal(b)
ans = floor(a*b)
print(ans)
