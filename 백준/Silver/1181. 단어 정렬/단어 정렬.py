import sys
input = sys.stdin.readline

n = int(input())

strings = []
for _ in range(n):
    strings.append(input().strip())

strings = list(set(strings))

result = []

for i in strings:
    result.append([len(i), i])

result.sort()

for j in result:
    print(j[1])