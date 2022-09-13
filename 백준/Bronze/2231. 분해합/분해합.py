import sys
input = sys.stdin.readline

n = int(input())

num = n
arr = []
while True :
    tmp = 0
    for i in str(num):
        tmp += int(i)
    
    if num + tmp == n:
        arr.append(num)
    
    elif num < 1:
        break
    
    
    num -= 1

if len(arr) > 0:
    print(min(arr))
else: print(0)