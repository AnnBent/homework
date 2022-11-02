import random
n = int(input("Введите кол-во строк матрицы: "))
m = int(input("Введите кол-во столбцов матрицы: "))
elem = 0
list1 = []
for i in range(n):
    list2 = []
    for j in range(m):
        list2.append(random.randint(-9, 9))
    list1.append(list2)
for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j], end="  ")
        if j < i:
            if list1[i][j] < 0:
                elem += 1
    print()
print("Кол-во отрицательных эл-тов под диагональю матрицы = ", elem)
