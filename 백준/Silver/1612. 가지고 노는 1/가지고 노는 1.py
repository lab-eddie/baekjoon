n = int(input())
i = 11
result = 2
if n == 1:
    print(1)
elif n % 2 == 0 or n % 5 == 0:
    print(-1)
else:
    while i % n != 0:
        i = i % n
        i = i * 10 + 1
        result += 1
    print(result)