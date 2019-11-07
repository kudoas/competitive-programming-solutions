n = int(input())
t, a = map(int, input().split())
H = list(map(int, input().split()))
ls = []

for h in H:
    ls.append(abs(a-(t-h*0.006)))

print(ls.index(min(ls))+1)
