n = int(input())

for i in range(n):
    ps = [_ for _ in input()]
    
    l = 0
    
    for j in ps:
        if ps[0] == ")":
            print("NO")
            break
        
        elif 