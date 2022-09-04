def fibonacci(n):
    if n == -1:
        return 1
    
    arr = [0, 1]
    
    for i in range(1, n+1):
        arr.append(arr[-2] + arr[-1])
    
    arr.pop(-1)
    return arr[-1]


t = int(input())

while t > 0:

    n = int(input())

    print(fibonacci(n-1),fibonacci(n))
    
    t -= 1