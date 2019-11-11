n, k = map(int, input().split())
ll = list(map(int, input().split()))
ll.sort(reverse=True)

print(sum(ll[:k]))
