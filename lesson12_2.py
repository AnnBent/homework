try:
    chislo = int(input("Введите число: "))
    n = len(str(chislo))
    stroka = str(chislo)
    for i in range(n-1, -1, -1):
        print(stroka[i], end=" ")
except ValueError:
    print("Вы ввели символы, а не цифры")