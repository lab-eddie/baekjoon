a = [i for i in input()]
b = [j for j in input()]

sorting = list(set(a) & set(b))

val = 0

for k in sorting:
    if a.count(k) >= b.count(k):
        val += b.count(k)
    else : val += a.count(k)
    

result = (len(a) - val) + (len(b) - val)

print(result)