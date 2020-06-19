x = int(input())
q, mod = divmod(x, 11)
if mod == 0:
    ans = q*2
elif mod <= 6:
    ans = q*2+1
else:
    ans = q*2+2
print(ans)
