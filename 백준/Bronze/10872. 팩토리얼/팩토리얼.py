import sys
input = sys.stdin.readline

n = int(input())

result = 1
while n != 0:
    result = result * n
    n -= 1
    
print(result)