try:
    n = int(input("Вычисление факториала\nВведите число: "))
    factorial = n
    while n != 1:
        factorial *= (n-1)
        n -= 1
    print("Факториал введённого числа равен ", factorial)
except ValueError:
    print("Вы ввели символы, а не цифры")