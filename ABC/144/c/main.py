n = int(input())
ls = []


for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        ls.append(i)
        if i != n // i:
            ls.append(n//i)
ls.sort()


i = len(ls)//2
j = i-1

if len(ls) % 2 == 1:
    print(ls[i]-1+ls[i]-1)
    exit()

print(ls[i]-1+ls[j]-1)
