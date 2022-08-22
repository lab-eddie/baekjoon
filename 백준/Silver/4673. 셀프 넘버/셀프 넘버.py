def self_number():
    li = []
    for i in range(1,10001):
        li.append(i + sum([int(j) for j in str(i)]))
    
    num = set(range(1,10001))
    result = num - set(li)
    result = list(result)
    result.sort()
    for i in result:
        print(i)
    

self_number()