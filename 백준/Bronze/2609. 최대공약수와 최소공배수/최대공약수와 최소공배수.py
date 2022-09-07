a, b = map(int, input().split())

n = 1
ali = []

while True:
    if n > a or n > b:
        break
    elif a % n == 0 and b % n == 0:
        ali.append(n)
    n += 1
g = max(ali)
m = g * (a / g) *(b / g)
print(g)
print(round(m))