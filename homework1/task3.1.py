# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Введите целое число от 1 до 4: "))
if quarter in range(1, 5):
    if quarter == 1:
        print("В первой четверти x > 0 и y > 0.")
    elif quarter == 2:
        print("Во второй четверти x < 0 и y > 0.")
    elif quarter == 3:
        print("В третьей четверти x < 0 и y < 0.")
    else:
        print("В четвёртой четверти x > 0 и y < 0.")
else:
    print("Не существует четверти с таким номером!")