n = int(input())
cnt = 0
while cnt < n:
    inp = input()
    result = 0
    point = 0
    for i in inp:
        if i == "O":
            point += 1
            result += point
        else : point = 0
    print(result)
    cnt += 1