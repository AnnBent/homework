import random
n = []
for i in range(0, 20):
    n.append(random.randint(0, 10))
print(n)
print("Удаление элементов, находящихся в интервале [2, 4]:")
for i in n:
    if 2 <= i <= 4:
        n.remove(i)
        n.append(0)
print(n)
