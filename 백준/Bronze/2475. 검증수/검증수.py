num = [int(_) for _ in input().split()]

result = 0
for i in num:
    result += i ** 2

print(result % 10)