import sys
input = sys.stdin.readline

text = input().strip().upper()

a = set(text)

result = []

for i in a:
    result.append([text.count(i), i])

result.sort()

try:
    if result[-1][0] == result[-2][0]:
        print("?")
    else:
        print(result[-1][1])
except:
    print(result[-1][1])