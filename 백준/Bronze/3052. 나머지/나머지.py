nums = set()
cnt = 0
while cnt < 10:
    inp = int(input())
    inp = inp % 42
    nums.add(inp)
    cnt += 1
print(len(nums))