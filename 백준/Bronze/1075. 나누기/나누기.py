import sys

n = input()
m = int(sys.stdin.readline())

def efficiency(num, portion):
       
    rest = num[-2:] # 뒤의 두자리를 나머지로 따로 빼주고
    num = int(num) - int(rest) # 뒤에 두자리를 00 으로 만들고
    if num % portion == 0: # 나눴을때 나머지가 0이면 값은 00 이 됨
        print("00")
        return
    else:
        result = portion - (num % m) # 나눠야할 숫자에서 위에서 나눈 나머지를 뺴주면 나눠지는 가장 작은수
        
    if len(str(result)) == 1: # 나온숫자가 1자리면 앞에 0을 붙여줌
        print(f"0{result}")
    else :
        print(result)
        
efficiency(n,m)