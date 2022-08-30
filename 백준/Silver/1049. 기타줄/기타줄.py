N, M = map(int, input().split())
arr = []
set = []
other = []
for i in range(M):
    arr.append(list(int (x) for x in input().split()))
arr.sort()

for el in arr:
    set.append(el[0])
    other.append(el[1])

set.sort()
other.sort()

sum = 0
set_min = set[0]
other_min = other[0]

if set_min >= other_min * 6:
    sum = other_min * N

else:
    if set_min < other_min:
        if N%6 == 0:
            sum = (set_min) * (N//6)
        else:
            sum = ((set_min) * (N // 6)) + set_min
    else:
        if N % 6 == 0:
            sum = (set_min) * (N // 6)
        else:
            other_price = (other_min) * int(N % 6)

            if other_price > set_min:
                sum = ((set_min) * (N // 6)) + set_min
            else:
                sum = ((set_min) * (N // 6)) + other_price

print(sum)

