import area_circle, area_triangle, area_rectangle

while True:
    print("\nВычисление площади\nкруга - клавиша 1\nпрямоугольника - клавиша 2\nтреугольника - клавиша 3")
    n = int(input("\nДля выхода из программы, нажмите 0\n"))
    if n == 1:
        r = int(input("Введите радиус круга: "))
        print("Площадь круга равна ", area_circle.circle(r))
    elif n == 2:
        a = int(input("Введите стороны прямоугольника\na = "))
        b = int(input("b = "))
        print("Площадь прямоугольника равна ", area_rectangle.rectangle(a, b))
    elif n == 3:
        h = int(input("Введите высоту треугольника h = "))
        c = int(input("Введите длину основания c = "))
        print("Площать треугольника равна ", area_triangle.triangle(h, c))
    elif n == 0:
        break
