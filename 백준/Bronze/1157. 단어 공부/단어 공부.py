inp = input().casefold()
s_inp = set(inp)
result = []
for i in s_inp:
    result.append([inp.count(i),i])
result.sort()
try :
    if result[-1][0] == result[-2][0]:
        print("?")
    else : print(result[-1][1].upper())
except:
    print(result[-1][1].upper())