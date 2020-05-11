n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
journey = [1]

for i in range(2*n+1000):
    nxt = a[journey[-1]]
    journey.append(nxt)

if k < n+1:
    print(journey[k])
    exit()

loop_end = n
loop_start = n-1

while(journey[loop_start] != journey[loop_end]):
    loop_start -= 1

period = loop_end-loop_start
k %= period

while k < n:
    k += period

print(journey[k])
