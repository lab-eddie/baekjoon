point = []
for i in range(5):
    p = int(input())
    if p < 40:
        p = 40
    else : pass
    
    point.append(p)

ave = round(sum(point) / 5)
print(ave)