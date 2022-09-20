import sys
input = sys.stdin.readline

alphabet = [_ for _ in "abcdefghijklmnopqrstuvwxyz".upper()]

text = input().strip()

result = 0
for i in text:
    if i in alphabet[0:3]: #2
        result += 3
    elif i in alphabet[3:6]: #3
        result += 4
    elif i in alphabet[6:9]: #4
        result += 5
    elif i in alphabet[9:12]: #5
        result += 6
    elif i in alphabet[12:15]: #6
        result += 7
    elif i in alphabet[15:19]: #7
        result += 8
    elif i in alphabet[19:22]: #8
        result += 9
    elif i in alphabet[22:]: #9
        result += 10

print(result)