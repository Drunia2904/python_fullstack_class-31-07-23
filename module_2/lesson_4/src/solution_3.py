price = float(input("Введите цену товара в долларах "))
current_course = float(input("Введите текущий курс доллара "))
price_in_rubles = price * current_course
print("Цена товара: " + str(round(price_in_rubles, 2)) + " руб.")