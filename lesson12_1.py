try:
    chislo = int(input("Введите пятизначное натуральное число: "))
    max_chislo = 0
    if 9999 < chislo < 100000:
        for i in range(0, 5):
            if int(str(chislo)[i]) > max_chislo:
                max_chislo = int(str(chislo)[i])
        print("Наибольшая цифра этого числа равна ", max_chislo)
    else:
        print("Вы ввели не пятизначное число")
except ValueError:
    print("Вы ввели символы, а не цифры")