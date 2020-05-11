import math

x = int(input())

i = 0
money = 100
while True:
    money = math.floor(money * 1.01)
    if money >= x:
        print(i+1)
        break
    i += 1
