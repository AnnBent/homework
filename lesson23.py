import random

numbers = list()


def random_array(a, b):
    for i in range(10):
        numbers.append(random.randint(a, b))


a = int(input("Введите диапазон значений: \na = "))
b = int(input("b = "))
random_array(a, b)
print(numbers)