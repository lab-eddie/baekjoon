import sys
input = sys.stdin.readline

n = int(input())
nums = [int(_) for _ in input().strip()]

result = 0
for num in nums:
    result += num

print(result)