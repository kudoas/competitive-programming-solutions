x = int(input())

yen_500 = x // 500
yen_50 = (x - yen_500 * 500) // 5
answer = yen_500*1000 + yen_50*5

print(answer)
