n = int(input())
cnt = 0
while cnt < n:
    point = list(map(int,input().split()))
    ave = sum(point[1:]) / point[0]
    good_person = []
    for i in point[1:]:
        if i > ave:
            good_person.append(i)
    print(f"{len(good_person) / point[0] * 100:.3f}%")
    cnt += 1