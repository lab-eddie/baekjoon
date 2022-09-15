m = int(input())
n = int(input())

arr = []

for i in range(101):
    val = i ** 2
    if val > n:
        break
    else :
        if m <= val <= n:
            arr.append(val)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))