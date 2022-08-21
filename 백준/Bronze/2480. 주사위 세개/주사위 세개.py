a,b,c = map(int,input().split())

if (a + b + c) / 3 == a:
    print(a*1000 + 10000)
elif a != b and b != c and a != c:
    big = 0
    for i in a,b,c:
        if big < i:
            big = i
    print(big*100)
else : 
    if a == b:
        print(a*100 + 1000)
    elif b == c:
        print(b*100 + 1000)
    else : 
        print(c*100 + 1000)