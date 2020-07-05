from collections import defaultdict

n = int(input())
d = defaultdict(int)
for _ in range(n):
    s = input()
    d[s] += 1
print('AC x '+str(d["AC"]))
print('WA x '+str(d["WA"]))
print('TLE x '+str(d["TLE"]))
print('RE x '+str(d["RE"]))
