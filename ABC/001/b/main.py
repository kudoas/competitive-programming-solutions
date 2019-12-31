m = int(input())

if m < 0.1:
    ans = 00
elif 0.1 <= m <= 5:
    ans = m+50
elif 6 <= m <= 30:
    ans = 10*m
elif 35 <= m <= 70:
    ans = (m-30)/5*80
elif 70 <= m:
    ans = 89

print(ans)
