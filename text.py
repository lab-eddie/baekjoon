import sys
input = sys.stdin.readline

n = int(input())

num = n

while True :
    tmp = 0
    for i in str(num):
        tmp += int(i)
    
    if num + tmp == n:
        print(num)
        break
    
    elif num + tmp < n:
        break
    
    else :
        num -= 1