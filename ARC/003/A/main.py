from collections import Counter

n = int(input())
C = Counter(list(input()))
gpa = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
ans = 0
for k, v in C.items():
    ans += gpa[k]*v
print(ans/n)
