alp = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
dial = [alp[:3],alp[3:6],alp[6:9],alp[9:12],alp[12:15],alp[15:19],alp[19:22],alp[22:]]
result = []
inp = input()
for n in inp:
    for i in dial:
        if n in i:
            result.append(dial.index(i)+3)
print(sum(result))
