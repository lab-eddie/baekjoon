n = int(input())
cnt = 0
point = list(map(int, input().split()))
ave = []
maxi = max(point)
for i in point:
    ave.append(i / maxi * 100)
print(sum(ave)/n)    