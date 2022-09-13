# import sys
# input = sys.stdin.readline

# a, b, v = map(int, input().split())
# cnt = 0

# while True:
#     cnt += 1
#     v = v - a
    
#     if v <= 0:
#         print(cnt)
#         break
#     else:
#         v = v + b

import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

result = v - a + 1