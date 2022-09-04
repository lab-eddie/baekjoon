n = int(input())

insu = 2

while n != 1:
    if n % insu == 0:
        print(insu)
        n = n / insu
    else :
        insu += 1