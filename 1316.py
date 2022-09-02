n = int(input())

cnt = 0

while 0 < n:
    word = [i for i in input()]
    
    check_word = set(word)
    
    for i in check_word:
        a = True
        tmp = []
        tmp.append([j for j, ele in enumerate(word) if ele == i])
        print(tmp)
        
        for k in tmp:
        
            if len(k) == 1 :
                pass
            else:
                if int(k[-1]) - int(k[0]) == len(tmp) - 1:
                    pass
                else : a = False
        
    if a:
        cnt += 1
        
    
        
    n -= 1

print(cnt)