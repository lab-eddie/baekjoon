n = int(input())
i = input()
result = 0
while n > 0:
    result += int(i[n-1])
    n -= 1
print(result)