n = int(input())

words = []
result = []
for _ in range(n):
    words.append(input())

for i in set(words):
    result.append([len(i),i])

result.sort()

for j in result:
    print(j[1])