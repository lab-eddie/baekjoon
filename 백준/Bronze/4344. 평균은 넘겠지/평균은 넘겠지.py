import sys
input = sys.stdin.readline

c = int(input())

for _ in range(c):
    
    tmp = [int(_) for _ in input().split()]
    
    person = tmp[0]
    points = tmp[1:]
    
    ave = sum(points) / person
    result = []
    for i in points:
        if i > ave:
            result.append(i)

    print(f"{(len(result) / person * 100):.3f}%")