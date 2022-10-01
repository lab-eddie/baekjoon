import sys
input = sys.stdin.readline

n = int(input())

xy = []
for _ in range(n):
    x, y = map(int, input().split())
    
    xy.append([x, y])

xy.sort()

for i in xy:
    print(" ".join(map(str, i)))