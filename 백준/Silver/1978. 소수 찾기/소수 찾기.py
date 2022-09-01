num_list = list(range(2,1001))
sosu = []
for i in num_list:
    for j in num_list:
        if i % j == 0 and i != j:
            break
        elif i % j == 0 and i == j:
            sosu.append(j)

n = int(input())
num = map(int,input().split())
cnt = 0
for i in num:
    if i in sosu:
        cnt += 1
    else : pass
print(cnt)