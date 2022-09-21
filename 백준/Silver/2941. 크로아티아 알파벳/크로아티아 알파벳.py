import sys
input = sys.stdin.readline

text = input().strip()

cro_alp = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in cro_alp:
    if i in text:
        text = text.replace(i,"*")

print(len(text))