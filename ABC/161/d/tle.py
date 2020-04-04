k = int(input())

if k <= 9:
    print(k)
    exit()

# 2桁以上の場合
cnt = 9
num = 0
moji = 0
while cnt < k:
    moji = str(num)
    for i in range(len(moji)-1):
        if abs(int(moji[i]) - int(moji[i+1])) > 1:
            break
        if i == len(moji)-2:
            cnt += 1
    num += 1

print(num-1)
