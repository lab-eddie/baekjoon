import sys
input = sys.stdin.readline

n = 1000 - int(input())
bill = [500, 100, 50, 10, 5, 1]

cnt = 0

for i in bill:
    
    if n == 0: break
    
    elif n >= i:
        cnt += n // i
        n = n - (i * (n // i))

print(cnt)