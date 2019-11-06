n = int(input())
# print(n//10*100+n % 10*15 if n % 10 <= 6 else ((n//10)+1)*100)
print(n//10*100+min(100, n % 10*15))
