n = int(input())

cnt = 0

while n > 0:
    inp = [i for i in input()]
    flag = True
    for j in set(inp):
        if inp.count(j) != 1:
            
            j_index = [k for k, e in enumerate(inp) if e == j]
            
            for l in range(len(j_index)):
                if l == len(j_index) - 1:
                    break
                else :
                    if j_index[l] + 1 != j_index[l+1]:
                        flag = False
                               
            
            
        else :
            pass
        
    if flag is True: cnt += 1
    else : pass
        
        
    n -= 1
    
print(cnt)