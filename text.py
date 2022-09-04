n = int(input())

arr = ["1","2","3"]

while n > 0:
    a, b = map(str, input().split())
    
    if 0 > int(a) > 3 or 0 > int(b) > 3:
        print(-1)
        quit()
        
    tmp1 = arr.index(a)
    tmp2 = arr.index(b)
    arr[tmp1] = b
    arr[tmp2] = a
    
    n -= 1

print(arr[0])