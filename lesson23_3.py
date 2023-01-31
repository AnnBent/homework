from math import pi


def circle(r):
    return pi * (r ** 2)


def rectangle(a, b):
    return a * b


def triangle(h, c):
    return h * c / 2


while True:
    print("\nВычисление площади\nкруга - клавиша 1\nпрямоугольника - клавиша 2\nтреугольника - клавиша 3")
    n = int(input("\nДля выхода из программы, нажмите 0\n"))
    if n == 1:
        r = int(input("Введите радиус круга: "))
        print("Площадь круга равна ", circle(r))
    elif n == 2:
        a = int(input("Введите стороны прямоугольника\na = "))
        b = int(input("b = "))
        print("Площадь прямоугольника равна ", rectangle(a, b))
    elif n == 3:
        h = int(input("Введите высоту треугольника h = "))
        c = int(input("Введите длину основания c = "))
        print("Площать треугольника равна ", triangle(h, c))
    elif n == 0:
        break
