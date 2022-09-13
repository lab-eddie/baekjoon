total = int(input())
qty = int(input())
for i in range(qty):
    a,b = map(int,input().split())
    total = total - (a*b)
total = "Yes" if total == 0 else "No"
print(total)