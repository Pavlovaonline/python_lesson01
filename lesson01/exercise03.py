try:
    x= int(input("Введите координаты x: "))
    y= int(input("Введите координаты y: "))
    if x > 0 and y > 0: print("Первая четверть")
    elif x < 0 and y > 0: print("Вторая четверть")
    elif x < 0 and y < 0: print("Третья четверть")
    elif x > 0 and y < 0: print("Четвертая четверть")
    elif x == 0 and y !=0: print("Точка находится на оси абсцисс")
    elif y == 0 and x !=0: print("Точка находится на оси ординат")
    elif x == 0 and y == 0: print("Начало координат")
except: print("Некорректные данные...")