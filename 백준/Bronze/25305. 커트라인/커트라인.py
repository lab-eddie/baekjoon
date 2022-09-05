n, k = map(int, input().split())

x = [int(i) for i in input().split()]
    
x.sort()

print(x[-k])