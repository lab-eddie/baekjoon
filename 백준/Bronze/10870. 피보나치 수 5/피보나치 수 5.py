n = int(input())
fibo = [0,1]
if n == 0:
    print(0)
    quit()
while n > 1:
    fibo.append(fibo[-1] + fibo[-2])
    n -= 1
print(fibo[-1])