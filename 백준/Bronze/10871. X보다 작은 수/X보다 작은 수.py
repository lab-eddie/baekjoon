n, x = map(int,input().split())
a = map(int,list(input().split()))
result = []
for i in a:
    if i < x:
        result.append(i)
    else:
        pass
print(*result)