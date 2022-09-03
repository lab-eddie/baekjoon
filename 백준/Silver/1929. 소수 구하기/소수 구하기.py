import math

a, b = map(int, input().split())

arr = [True for i in range(b+1)]
arr[1] = False
for i in range(2, int(math.sqrt(b)) + 1):
    if arr[i] == True:
        
        j = 2
        
        while i * j <= b:
            arr[i * j] = False
            j += 1

result = [i for i in range(a, b+1) if arr[i]]

for k in result:
    print(k)