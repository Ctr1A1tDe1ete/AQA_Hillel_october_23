products = input("Введите добавляемые товары")
list = products.split()
print(list)

for i in range(5):
    x = int(input("Введите номер товара"))
    list.pop(x - 1)
    print(list)

if len(list) == 0:
    print("Ваша корзина пуста")
else:
    print("У вас в корзине еще есть не купленные товары")

products_add = input("Какие товары вы хотите добавить в корзину еще?")
list = products_add.split()
print(list)
print("Всего доброго! хорошего, Вам, чего бы  там  у вас ни было!")
