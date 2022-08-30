chess = []
for lines in range(8):
    chess.append(input())
    
cnt = -1
result = 0
for i in chess:
    cnt += 1
    for j in enumerate(i):
        
        if (cnt % 2 == 0) and (j[0] % 2 == 0) and (j[1] == "F"):
            result += 1
            
        elif (cnt % 2 != 0) and (j[0] % 2 != 0) and (j[1] == "F"):
            result += 1
            
        else : continue

print(result)