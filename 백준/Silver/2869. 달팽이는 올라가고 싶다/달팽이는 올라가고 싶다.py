import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())
import math
print(math.ceil((v - a) / (a - b) + 1))