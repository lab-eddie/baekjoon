import sys
input = sys.stdin.readline

alphabet = [_ for _ in "abcdefghijklmnopqrstuvwxyz"]

text = [_ for _ in input().strip()]

result = []

for i in alphabet:
    if i in text:
        result.append(text.index(i))
    else:
        result.append(-1)

print(" ".join(map(str, result)))