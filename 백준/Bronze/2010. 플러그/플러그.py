import sys
input = sys.stdin.readline

n = int(input())
result = 1
for _ in range(n):
    plug = int(input())
    result += (plug - 1)

print(result)