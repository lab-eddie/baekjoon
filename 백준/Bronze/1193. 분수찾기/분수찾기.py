x = int(input())

line = 0
while x > line:
    x -= line
    
    line += 1

num_list_1 = list(range(1, line+1))
num_list_2 = num_list_1[::-1]

if line % 2 == 0:
    print(f"{num_list_1[x-1]}/{num_list_2[x-1]}")
else:
    print(f"{num_list_2[x-1]}/{num_list_1[x-1]}")