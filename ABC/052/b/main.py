n = int(input())
s = input()

ans = 0
ls = [0]

for i in s:
    if i == 'I':
        ans += 1
    else:
        ans -= 1
    ls.append(ans)

print(max(ls))
