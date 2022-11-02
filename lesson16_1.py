import random
list1 = []
n = int(input("Введите кол-во строк матрицы: "))
m = int(input("Введите кол-во столбцов матрицы: "))
elem = 0
for i in range(n):
    list2 = []
    for j in range(m):
        list2.append(random.randint(0, 9))
    list1.append(list2)
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if i == j:
            if list1[i][i] > elem:
                elem = list1[i][i]
        print(list1[i][j], end=" ")
    print()
print(elem)
