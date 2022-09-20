n = int(input())
while n:
    result = []
    inp = input().split()
    for i in inp[-1]:
        result.append(i * int(inp[0]))
    print("".join(result))
    n -= 1
