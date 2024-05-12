# Написати програму, яка зчитує два числа та виводить їхню суму, різницю, добуток та частку.

def addition(a: int, b: int):
    result = print(a + b)
    return result


def subtraction(a: int, b: int):
    result = print(a - b)
    return result


def multiplication(a: int, b: int):
    result = print(a * b)
    return result


def division(a: int, b: int):
    result = print(a / b)
    return result


addition(a=3, b=4)
subtraction(a=32, b=23)
multiplication(a=6, b=8)
division(a=15, b=3)


# Напишіть за допомогою f-string та format. Дві стрічки де буде підставлятись імя та вік з зміних
# name = "оЛенА"
# age = 21
# f_string = тут ваш код формата ф-стрінг. | повино вийти -> Я Олена, мені 21 рік
# format_string = тут ваш код формата формат стрінг | повино вийти -> Я Олена, мені 21 рік
# print(f_string)
# print(format_string)

def foo(name, age):
    f_string = print(f"Я {name.capitalize()}, мне {age} год")
    format_string = print("Я {}, мне {} год".format(name.capitalize(), age))
    return f_string, format_string


foo(name="оЛенА", age=21)
