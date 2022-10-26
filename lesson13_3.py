minimal = int(input("Введите минимальное число: "))
maximal = int(input("Введите максимальное число: "))
summa = 0
for i in range(minimal+1, maximal):
    summa += i
print("Сумма элементов, находящихся между минимальным и максимальным значением равна ", summa)

