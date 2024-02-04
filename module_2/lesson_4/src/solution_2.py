length: float = float(input("Введите длину помещения, метров "))
width: float = float(input("Введите ширину помещения, метров "))
area: float = length * width
print("Площадь помещения равна " + str(round(area, 2)) + " м^2")