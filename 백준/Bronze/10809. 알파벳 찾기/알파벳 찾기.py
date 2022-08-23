s = input()
alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
result = []
for i in alphabet:
    if i in s:
        result.append(s.index(i))
    else : result.append(-1)
print(" ".join(map(str,result)))