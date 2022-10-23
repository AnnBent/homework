try:
    chislo = int(input("Введите трёхзначное натуральное число: "))
    if 99 < chislo < 1000:
        s = int(str(chislo)[0]) + int(str(chislo)[1]) + int(str(chislo)[2])
        mul = int(str(chislo)[0]) * int(str(chislo)[1]) * int(str(chislo)[2])
        print("Сумма цифр введённого числа: ", s)
        print("Произведение цифр введённого числа: ", mul)
    else:
        print("Вы ввели не трёхзначное число")

except ValueError:
    print("Вы ввели символы, а не число")