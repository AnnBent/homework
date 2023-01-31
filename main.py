import figure_area

while True:
    print("\nВычисление площади\nкруга - клавиша 1\nпрямоугольника - клавиша 2\nтреугольника - клавиша 3")
    n = int(input("\nДля выхода из программы, нажмите 0\n"))
    if n == 1:
        r = int(input("Введите радиус круга: "))
        print("Площадь круга равна ", figure_area.circle(r))
    elif n == 2:
        a = int(input("Введите стороны прямоугольника\na = "))
        b = int(input("b = "))
        print("Площадь прямоугольника равна ", figure_area.rectangle(a, b))
    elif n == 3:
        h = int(input("Введите высоту треугольника h = "))
        c = int(input("Введите длину основания c = "))
        print("Площать треугольника равна ", figure_area.triangle(h, c))
    elif n == 0:
        break
