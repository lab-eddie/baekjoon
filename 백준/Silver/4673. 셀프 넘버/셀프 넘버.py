import sys
input = sys.stdin.readline

arr = [_ for _ in range(1,10001)]
not_self = []
for i in arr:
    tmp = 0
    for j in str(i):
        tmp += int(j)
    not_self.append(i + tmp)

self_num = set(arr)-set(not_self)

a = list(self_num)
a.sort()

for k in a:
    print(k)