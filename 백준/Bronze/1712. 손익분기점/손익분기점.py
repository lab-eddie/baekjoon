import math
fix, vari, price = map(int,input().split())
if vari >= price :
    print(-1)
    quit()
bep = fix / (price-vari)
if fix % (price - vari) == 0:
    print(round(bep + 1))
else : print(math.ceil(bep))