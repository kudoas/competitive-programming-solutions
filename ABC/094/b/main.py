n, m, x = map(int, input().split())
a = list(map(int, input().split()))

right = len([int(i) for i in a if x < i])
# left = len([int(i) for i in a if x > i])
left = m-right

print(min(right, left))
