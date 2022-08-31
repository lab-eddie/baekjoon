x, y, w, h = map(int, input().split())

garo = x - 0 if x - 0 <= w - x else w - x
sero = y - 0 if y - 0 <= h - y else h - y

rst = [garo, sero]

print(min(rst))