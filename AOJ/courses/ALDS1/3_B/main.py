from collections import deque

# Round robin scheduling
n, q = map(int, input().split())
queue = deque()
for _ in range(n):
    n, t = input().split()
    queue.append([n, int(t)])
time = 0
finish = []
while len(queue) > 0:
    l = queue.popleft()
    cost = min(q, l[1])
    l[1] -= cost
    time += cost
    if l[1] == 0:
        finish.append((l[0], time))
    else:
        queue.append(l)
for f in finish:
    print(*f)
