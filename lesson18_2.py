import random
n = int(input("Введите количество множеств: "))
list1 = list()
list2 = list()
result = set()
if n > 0:
    # создание множеств
    for i in range(1, n+1):
        set0 = set()
        for j in range(10):
            set0.add(random.randint(-10, 10))
        list1.append(set0)
        if i%3 == 0:
            list2.append(set0)
        if i == 1:
            set1 = set0
    for i in list1:
        print(i)
    for i in list2:
        for j in i:
            result.add(j)
    print("Ответ на вопрос:")
    print(result.difference(set1))

else:
    print("Введите корректное значение!")
