import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [int(_) for _ in input().split()]

for i in range(m):
    result = 0
    i, j = map(int, input().split())

    for j in arr[i-1:j]:
        result += j
    
    print(result)