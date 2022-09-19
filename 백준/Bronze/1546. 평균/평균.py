import sys
input = sys.stdin.readline

n = int(input())

point = [int(_) for _ in input().split()]

m = max(point)

result = []
for i in point:
    result.append(i / m * 100)

print(sum(result) / n)