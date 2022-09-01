color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

val = []
for i in range(3):
    val.append(input())

resist = f"{color.index(val[0])}{color.index(val[1])}"

result = int(resist) * int(("1" + "0" * color.index(val[2])))
print(result)