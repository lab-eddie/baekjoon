import sys

def merge_list(bin_list):
    if len(bin_list) <= 1:
        return bin_list

    mid = len(bin_list) // 2
    left = bin_list[:mid]
    right = bin_list[mid:]

    left_list = merge_list(left)
    right_list = merge_list(right)
    return sort(left_list, right_list)

def sort(left_list, right_list):
    result = []
    i = 0
    j = 0

    while (i < len(left_list)) and (j < len(right_list)):
        if left_list[i] < right_list[j]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1
    while (i < len(left_list)):
        result.append(left_list[i])
        i += 1
    while (j < len(right_list)):
        result.append(right_list[j])
        j += 1
    return (result)

N = int(input())
bin_list = []

for _ in range(N):
    bin_list.append(int(sys.stdin.readline()))

bin_list = merge_list(bin_list)

for i in bin_list:
    print(i)