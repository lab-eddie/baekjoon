n = input()

y = n
cnt = 0
num = None
if len(n) == 1:
    n = n + "0"
while True:
    if num == y:
        break
    cnt += 1
    try :
        a1, a2 = int(n[0]), int(n[1])
        num = a1 + a2
        num = str(num)
    except :
        a2 = int(n[0])
    n = str(a2) + num[-1]
print(cnt)
        