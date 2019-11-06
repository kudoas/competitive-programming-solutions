n, l = map(int, input().split())
ls = [i+l-1 for i in range(1, n+1)]

ls.remove(min(ls, key=abs))
print(sum(ls))
