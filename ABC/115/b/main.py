n = int(input())
ls = [int(input()) for _ in range(n)]

print(round(sum(ls)-(max(ls))/2))
