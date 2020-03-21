
s = input()
k = int(input())

# 1の連続性を確認し終わった段階の数字を記録
cnt = 0

for i in range(len(s)):
    if s[i] != '1':
        num = s[i]
        break
    if s[i] == '1':
        cnt += 1

if cnt >= k:
    print(1)
else:
    print(num)
