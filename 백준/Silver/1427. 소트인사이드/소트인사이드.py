import sys
input = sys.stdin.readline

val = [int(_) for _ in input().strip()]

val.sort(reverse=True)

result = []

for i in val:
    result.append(str(i))
    
print("".join(result))