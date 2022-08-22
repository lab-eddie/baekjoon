numbers = []
cnt = 0
while cnt < 9:
    inp = int(input())
    numbers.append(inp)
    cnt += 1
print(f"{max(numbers)}\n{numbers.index(max(numbers))+1}")