n = int(input())

pattern = input()
result = [p for p in pattern]

for j in range(n-1):
    inp = input()
    for i in range(len(inp)):
        if inp[i] != pattern[i]:
            result[i] = "?"
        else: pass

print("".join(result))