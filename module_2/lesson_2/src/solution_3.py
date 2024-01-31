books = int(input("Введите количество коробок книг "))
stationery = int(input("Введите количество коробок канцтоваров "))
toys = int(input("Введите количество коробок игрушек "))
total_books = books * 2
total_stationery = stationery * 1.5
total_toys = toys * 3
total_size = total_books + total_stationery + total_toys
print("Общий объём: " + str(total_size) + " м^3")