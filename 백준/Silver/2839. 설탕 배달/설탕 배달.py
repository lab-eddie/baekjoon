n = int(input())

result = 0

if n % 5 == 0:
    result = n // 5

tmp = n // 5
while True:
    if tmp == -1:
        print(-1)
        break
    
    rest = n - (5 * tmp)
    if rest % 3 == 0:
        result = tmp + (rest // 3)
        print(result)
        break
    
    else :
        tmp -= 1