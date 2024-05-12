PIN = 4444
n = 2
print("Введите пароль:")
while True:
    PIN = int(input())
    if PIN == 4444:
        print("Вы успешно вошли")
        break
    else:
        if PIN != 4444 and n > 0:
            print("Некорректный PIN!")
            print("Введите пароль:")
            n = n - 1
        else:
            print("Карта заблокирована")
            break
