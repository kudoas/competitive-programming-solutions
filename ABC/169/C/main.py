# from math import floor
# import decimal

# a, b = input().split()
# a = decimal.Decimal(a)
# b = decimal.Decimal(b)
# ans = floor(a*b)
# print(ans)

from math import floor

a, b = map(float, input().split())
a = int(a)
b *= 100
b = round(b)
print(a*b//100)
