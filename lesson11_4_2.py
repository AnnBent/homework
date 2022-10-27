try:
    minimal = int(input("Введите минимальное натуральное число: "))
    maximal = int(input("Введите максимальное натуральное число: "))
    step = int(input("Введите шаг: "))
    if minimal > maximal:
        print("Минимальное число не может быть больше максимального")
    elif minimal <= 0 or maximal <= 0 or step <= 0:
        print("Вы ввели не натуральные числа")
    else:
        for i in range(minimal, maximal+1, step):
            print(i, end = ' ')
except ValueError:
    print("Вы ввели символы, а не число")



