def summa(chislo):
    if chislo == 0:
        return 0
    return chislo % 10 + summa(chislo // 10)


chislo = int(input("Введите число "))

print("Сумма цифр числв равна ", summa(chislo))
