import sys
input = sys.stdin.readline

arr = []
for _ in range(10):
    a = int(input())
    arr.append(a % 42)

result = set(arr)

print(len(result))