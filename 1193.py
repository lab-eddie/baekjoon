n = int(input())

cnt = 1
a = 1
arr = []
for i in range(n):
    arr.append([j for j in range(cnt,cnt+a)])
    
    cnt = cnt + a
    
    a += 1
    

arr.index()