math_dict = {"+": {}, "*": {}, "-": {}, "/": {}}

for i in range(2, 10):
    for j in range(2, 10):
        math_dict["+"][i, j] = f"{i}+{j}={i + j}"
        math_dict["*"][i, j] = f"{i}*{j}={i * j}"
        math_dict["-"][i, j] = f"{i}-{j}={i - j}"
        math_dict["/"][i, j] = f"{i}/{j}={round((i / j), 2)}"

user_choice = input("Яку таблицю ви хочете бачити? Введіть: '+','-','*' або '/':")

if user_choice == "+":
    for i in math_dict["+"]:
        print(math_dict["+"][i])
elif user_choice == "*":
    for i in math_dict["*"]:
        print(math_dict["*"][i])
elif user_choice == "-":
    for i in math_dict["-"]:
        print(math_dict["-"][i])
elif user_choice == "/":
    for i in math_dict["/"]:
        print(math_dict["/"][i])
else:
    print("Такої операції немає")
