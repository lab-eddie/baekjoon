import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

day = (v - a) / (a - b) + 1

import math
print(math.ceil(day))