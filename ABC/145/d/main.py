from numpy import array
import math

x, y = map(int, input().split())

target = array([x, y], 3*(math.sqrt(2)))
v1 = array([1, 2], )
v2 = array([2, 1])

ans = array([0, 0])
cnt = 0

while ans[0] > x or ans[1] > y:
