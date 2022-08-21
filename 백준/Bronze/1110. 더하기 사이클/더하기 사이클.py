n = input()
if len(n) == 1:
    n = n + "0"
y = n
cnt = 0
while True:
    try :
        a1, a2 = int(n[0]), int(n[1])
        nu = a1 + a2
        nu = str(nu)
    except :
        a2 = int(n[0])
    n = str(a2) + nu[-1]
    cnt += 1
    if n == y:
        break
print(cnt)