import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    
    test = [_ for _ in input().strip()]
    
    result = 0
    cnt = 0
    for i in test:
        if i == 'O':
            cnt += 1
        elif i == 'X':
            cnt = 0
        
        result += cnt

    print(result)