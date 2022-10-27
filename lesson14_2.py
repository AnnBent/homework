import random
n = []
summa = 0
for i in range(0, 10):
    n.append(random.randint(0, 10))
    i += 1
print(n)
for i in n:
    summa += i
summa /= 10
print("Среднее арифметическое элементов = ", int(summa))
print("Элементы, значение которых меньше среднего арифметического: ")
for i in n:
    if i < summa:
        print(i, end=" ")

