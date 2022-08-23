inp = input().split()
result = 0
for i in inp:
    num = int(i[::-1])
    if num > result:
        result = num
print(result)