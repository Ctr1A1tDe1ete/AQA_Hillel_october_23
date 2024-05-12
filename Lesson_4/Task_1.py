price = input("Введите стоимость товаров")
price = price.split()
new_price_list = []
for element in price:
    element = float(element)
    if isinstance(element, (int, float)):
        new_price_list.append(element + element * 0.065)
total = sum(new_price_list)

discount = int(input("введите 1, если у вас  есть скидочный купон"))
if discount == 1:
    discount_type = int(input("введите 1, если скидка на сумму или 2, если скидка на процент"))
    if discount_type == 1:
        discount_type_1 = float(input("введите размер скидки"))
        final_price = total - discount_type_1
        print("Сумма к оплате", (final_price))
    else:
        discount_type_2 = float(input("введите процент скидки"))
        final_price = total - (total / 100 * discount_type_2)
        print("Сумма к оплате", (final_price))

#  завдання з зірочкою не впливає на бал. Округліть суму якщо копійок більше ніж 44 то це буде + 1 гривня,
# якщо менше. то тоді просто відкидаємо копійки від ціни.
import math
residual = final_price - int(final_price)
if residual >= 0.44:
    final_price = math.ceil(final_price)
else:
    final_price = (math.floor(final_price))
print("Округленная сумма к оплате", (final_price))


