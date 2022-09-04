hours = list(range(0,24))
minutes = list(range(0,60))
a, b = map(int, input().split())

if b - 45 < 0:
    a = hours[a-1]
b = minutes[b-45]

print(a,b)