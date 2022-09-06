n, m = map(int, input().split())
arr = [int(i) for i in input().split()]
l = len(arr)
result = 0

for i in range(0, l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            jack = arr[i] + arr[j] + arr[k]
            if jack > m:
                continue
            else:
                result = max(result, jack)
    
print(result)