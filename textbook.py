a, b, v = map(int, input().split())
h = 0
cnt = 0
flag = True
while flag:
    h += a
    if v <= h:
        flag = False
    else :
        h -= b
    
    cnt += 1

print(cnt)

