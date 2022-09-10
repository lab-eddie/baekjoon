a = int(input())
b = int(input())
c = int(input())

result = a * b * c

result = [int(_) for _ in str(result)]

for i in range(0,10):
    print(result.count(i))