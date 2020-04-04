n = int(input())
card = list('123456')

# 30回で元に戻る
n %= 30

for i in range(n):
    num = i % 5
    card[num], card[num+1] = card[num+1], card[num]

print(''.join(card))
