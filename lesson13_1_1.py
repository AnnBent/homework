try:
    n = int(input("Введите количество элементов ряда Фибоначчи: "))
    if n < 0:
        print("Количество элементов не может быть меньше нуля!")
    elif n == 0:
        print(0)
    else:
        fib1 = 1
        fib2 = 2
        print(fib1, fib2, end=" ")
        while n > 0:
            fibsum = fib1 + fib2
            fib1 = fib2
            fib2 = fibsum
            print(fibsum, end=' ')
            n -= 1

except ValueError:
    print("Вы ввели символы, а не цифры")
