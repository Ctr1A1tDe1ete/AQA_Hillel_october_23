var_1 = input("введіть перше значення")
var_2 = input("введіть друге значення")


question = input("це int або str")

if question == "int":
    print((int(var_1) + int(var_2)) * 3)

else:
    print(int(var_1 + var_2) * 3)