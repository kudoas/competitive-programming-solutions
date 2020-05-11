n, m = map(int, input().split())
A = [int(input()) for _ in range(m)][::-1]
thread = []
visited = set()

for a in A:
    if a in visited:
        continue
    visited.add(a)
    thread.append(a)

for i in range(1, n+1):
    if i in visited:
        continue
    thread.append(i)

print(*thread, sep='\n')
