n, m = map(int, input().split())
string = []
for _ in range(n):
    string.append(input())

cnt = 0

while m > 0:
    check = input()
    if check in string:
        cnt += 1
    else : pass
    
    m -= 1

print(cnt)