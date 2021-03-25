# round robin scheduling
from collections import deque

n, q = map(int, input().split())
queue = deque()
for _ in range(n):
    queue.append(list(input().split()))

total = 0
while len(queue) != 0:
    name, time = queue.popleft()
    time = int(time)
    need_time = min(time, q)
    total += need_time
    if time == need_time:
        print(name, total)
        continue
    queue.append([name, time-need_time])
