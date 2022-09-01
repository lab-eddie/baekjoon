import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    base = a % 10
   
    if base == 0:
        print(10)
    
    elif base in [1,5,6]:
        print(base)
    
    elif base in [4,9]:
        if b % 2 == 0:
            print((base ** 2) % 10)
        else:
            print(base)
    elif base in [2,3,7,8]:
        if b % 4 == 0:
            print((base ** 4) % 10)
        else:
            b = b % 4
            print((base ** b) % 10)