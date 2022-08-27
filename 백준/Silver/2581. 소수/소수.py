m = int(input())
n = int(input())

result = []

for i in range(m, n + 1):
    err = 0
    if i > 1 :
        for j in range(2, i):
            if i % j == 0:
                err += 1
        if err == 0:
            result.append(i)
   

if result == []:
    print(-1)
else :
    print(sum(result))
    print(min(result))