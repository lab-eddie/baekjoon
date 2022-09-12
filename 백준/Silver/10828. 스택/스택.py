import sys
input = sys.stdin.readline
n = int(input())
stack = []

for _ in range(n):
    inp = input().split()
    
    if inp[0] == "push":
        stack.append(inp[1])
    elif inp[0] == "pop":
        try:
            a = stack.pop()
            print(a)
        except:
            print(-1)
    elif inp[0] == "size":
        print(len(stack))
    elif inp[0] == "empty":
        if len(stack) >= 1:
            print(0)
        else: print(1)
    elif inp[0] == "top":
        try:
            print(stack[-1])
        except:
            print(-1)